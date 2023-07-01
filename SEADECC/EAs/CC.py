import numpy as np
from EAs import helps


def CC_exe(Dim, scale_range, NIND, groups, Max_iter, func, Optimizer):
    Pop = helps.InitialPop(Dim, scale_range, NIND)
    context = np.zeros(Dim)
    for group in groups:
        subPop = helps.SubPop(Pop, group)
        bestSubPop = Optimizer(subPop, group, func, context, Max_iter, scale_range)
        for i in range(len(group)):
            context[group[i]] = bestSubPop[i]
    return [func(context)]


