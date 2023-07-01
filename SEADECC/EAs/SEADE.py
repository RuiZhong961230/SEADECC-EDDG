import numpy as np
from random import sample
from EAs.helps import CheckIndi
from sklearn.preprocessing import MinMaxScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as CK
from EAs import helps
from copy import deepcopy
from pyGRNN import GRNN


def embed(context, group, data):
    solution = deepcopy(context)
    for i in range(len(group)):
        solution[group[i]] = data[i]
    return solution


def Estimation(X, y, Archive, Archive_Fit, context, group):
    search_space = scales(X)
    scale = MinMaxScaler()
    y_scale = scale.fit_transform(np.array(y).reshape(-1, 1))
    Archive_Fit_scale = scale.fit_transform(np.array(Archive_Fit).reshape(-1, 1))

    grnn = GRNN()
    grnn.fit(Archive, Archive_Fit_scale)
    grnn_x = Minimization(grnn, search_space)

    mixed_kernel = CK(1.0, (1e-4, 1e4)) * RBF(10, (1e-4, 1e4))
    gpr = GaussianProcessRegressor(n_restarts_optimizer=20, kernel=mixed_kernel)
    gpr.fit(X, y_scale)
    gpr_x = Minimization(gpr, search_space)

    return embed(context, group, grnn_x), embed(context, group, gpr_x)


def scales(data):
    data = np.array(data)
    limit_scale = []
    for i in range(len(data[0])):
        d = data[:, i]
        limit_scale.append([min(d), max(d)])
    return limit_scale


class Model:
    def __init__(self, model, dim):
        self.model = model
        self.dim = dim

    def predict(self, x):
        X = np.array([x]).reshape(-1, self.dim)
        label = self.model.predict(X)
        return label


def generate(scale_range, size):
    Dim = len(scale_range)
    solutions = np.zeros((size, Dim))
    for i in range(size):
        for j in range(Dim):
            solutions[i][j] = np.random.uniform(scale_range[j][0], scale_range[j][1])
    return solutions


def Minimization(model, scale_range):
    solutions = generate(scale_range, 1000)  # Random search
    Fit = model.predict(solutions)
    return solutions[np.argmin(Fit)]


def SEADE_exe(subPop, group, func, context, Max_iter, scale_range):
    F = 0.8
    Cr = 0.5
    NIND = len(subPop)
    tPop = np.array([context] * NIND)
    candidates = list(range(NIND))

    # Embedding the sub-population to context vector
    for i in range(len(group)):
        tPop[:, group[i]] = subPop[:, i]
    tPopFit = np.zeros(NIND)
    for i in range(NIND):
        tPopFit[i] = func(tPop[i])

    # Optimization
    Archive = deepcopy(subPop)
    Archive_Fit = deepcopy(tPopFit)
    for i in range(Max_iter):
        Off = np.array([context] * NIND)
        OffFit = np.zeros(NIND)

        # Mutation
        for j in range(NIND - 2):
            r1, r2, r3 = sample(candidates, 3)
            Off[j] = tPop[r1] + F * (tPop[r2] - tPop[r3])
            CheckIndi(Off[j], scale_range)

        # Crossover
        for j in range(NIND - 2):
            jrand = np.random.randint(0, len(context))
            for k in range(len(context)):
                if np.random.rand() < Cr or k == jrand:
                    Off[j][k] = tPop[j][k]

        tsubpop = helps.SubPop(tPop, group)
        Off[NIND - 2], Off[NIND - 1] = Estimation(tsubpop, tPopFit, Archive, Archive_Fit, context, group)

        # Selection
        for j in range(NIND):
            OffFit[j] = func(Off[j])

            # Add to archive
            np.append(Archive, deepcopy(Off[j]))
            np.append(Archive_Fit, OffFit[j])
            if OffFit[j] < tPopFit[j]:
                tPop[j] = Off[j]
                tPopFit[j] = OffFit[j]

    bestPop = tPop[np.argmin(tPopFit)]
    bestSubPop = np.zeros(len(group))
    for i in range(len(group)):
        bestSubPop[i] = bestPop[group[i]]
    return bestSubPop

