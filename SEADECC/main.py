import numpy as np
from Grouping.Methods import EDDG
from os import path
from cec2013lsgo.cec2013 import Benchmark
from EAs.CC import CC_exe
from EAs.SEADE import SEADE_exe
import warnings

warnings.filterwarnings('ignore')


def Write(data, path):
    with open(path, "a+") as file:
        np.savetxt(file, data, delimiter=",")
        file.close()


if __name__ == "__main__":
    Dims = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 905, 905, 1000]

    bench = Benchmark()
    this_path = path.realpath(__file__)

    NIND = 10
    trial = 25
    EDDG_cost = [2998, 2998, 3996, 5330, 5617, 5742, 5444, 8019, 8885, 8655, 9296, 29100, 7583, 8170, 3996]

    for func_num in range(7, 8):
        Dim = Dims[func_num-1]
        FEs = Dim * 100
        func = bench.get_function(func_num)
        info = bench.get_info(func_num)
        scale_range = [info["lower"], info["upper"]]

        SEADE_EDDG_obj_path = path.dirname(this_path) + "/Data/SEADECC-EDDG/" + str(func_num) + ".csv"
        EDDG_Max_iter = int((FEs - EDDG_cost[func_num-1]) / Dim / NIND)
        EDDG_groups = EDDG(path.dirname(this_path) + "/EDDG/f" + str(func_num) + ".mat")

        for i in range(trial):
            SEA_EDDG_obj = CC_exe(Dim, scale_range, NIND, EDDG_groups, EDDG_Max_iter, func, SEADE_exe)
            Write(SEA_EDDG_obj, SADE_EDDG_obj_path)








