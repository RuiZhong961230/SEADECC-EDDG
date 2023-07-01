import numpy as np


def InitialPop(Dim, scale_range, NIND):
    Pop = np.zeros((NIND, Dim))
    for i in range(NIND):
        for j in range(Dim):
            Pop[i][j] = np.random.uniform(scale_range[0], scale_range[1])
    return Pop


def CheckIndi(Indi, scale_range):
    range_width = scale_range[1] - scale_range[0]
    Dim = len(Indi)
    for i in range(Dim):
        if Indi[i] > scale_range[1]:
            n = int((Indi[i] - scale_range[1]) / range_width)
            mirrorRange = (Indi[i] - scale_range[1]) - (n * range_width)
            Indi[i] = scale_range[1] - mirrorRange
        elif Indi[i] < scale_range[0]:
            n = int((scale_range[0] - Indi[i]) / range_width)
            mirrorRange = (scale_range[0] - Indi[i]) - (n * range_width)
            Indi[i] = scale_range[0] + mirrorRange
        else:
            pass


def SubPop(Pop, group):
    subpop = np.zeros((len(Pop), len(group)))
    for i in range(len(group)):
        subpop[:, i] = Pop[:, group[i]]
    return subpop


