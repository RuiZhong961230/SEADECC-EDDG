import numpy as np
from random import sample
from EAs.helps import CheckIndi


def DE_exe(subPop, group, func, context, Max_iter, scale_range):
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
    for i in range(Max_iter):
        Off = np.array([context] * NIND)
        OffFit = np.zeros(NIND)

        # Mutation
        for j in range(NIND):
            r1, r2, r3 = sample(candidates, 3)
            Off[j] = tPop[r1] + F * (tPop[r2] - tPop[r3])
            CheckIndi(Off[j], scale_range)

        # Crossover
        for j in range(NIND):
            for k in range(len(context)):
                if np.random.rand() < Cr:
                    Off[j][k] = tPop[j][k]

        # Selection
        for i in range(NIND):
            OffFit[i] = func(Off[i])
            if OffFit[i] < tPopFit[i]:
                tPop[i] = Off[i]
                tPopFit[i] = OffFit[i]

    bestPop = tPop[np.argmin(tPopFit)]
    bestSubPop = np.zeros(len(group))
    for i in range(len(group)):
        bestSubPop[i] = bestPop[group[i]]
    return bestSubPop

