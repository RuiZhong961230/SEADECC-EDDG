import numpy as np
import scipy.io as sio


# This program reads the decomposition of EDDG by matlab.
def EDDG(ERDG_path):
    ERDG_groups = list(sio.loadmat(ERDG_path)['groups'])
    groups = []
    for i in range(len(ERDG_groups)):
        temp = list(ERDG_groups[i][0][0])
        for j in range(len(temp)):
            temp[j] -= 1
        for j in range(int(len(temp) / 100) + 1):
            start = j * 100
            end = min((j + 1) * 100, len(temp))
            if len(temp[start: end]) != 0:
                groups.append(temp[start: end])
    return groups

