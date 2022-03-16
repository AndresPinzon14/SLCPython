import numpy as np
import scipy.stats as stats
from SLCfiles.ShareSettings import ProblemSettings
from SLCfiles.ShareSettings import SCASettings
from SLCfiles.Thakhsis import Takhsis
from SLCfiles.UpdateTotalCost import UpdateTotalCost


def CreateInitialLeague():
    CostFunction = ProblemSettings["CostFunction"]
    VarSize = ProblemSettings["VarSize"]
    VarMin = ProblemSettings["VarMin"]
    VarMax = ProblemSettings["VarMax"]
    nVar = ProblemSettings["nVar"]
    De = ProblemSettings["De"]
    nTeam = SCASettings["nTeam"]
    nMainPlayer = SCASettings["nMainPlayer"]
    nReservePlayer = SCASettings["nReservePlayer"]
    League = [{"MPlayer": [{"Position": [None]*nVar, "Cost":None}]*nMainPlayer,
               "RPlayer":[{"Position": [None]*nVar, "Cost":None}]*nReservePlayer}]*nTeam
    for j in np.arange(0, nTeam):
        for i in np.arange(0, nMainPlayer):
            XY = np.floor(stats.uniform.rvs(VarMin, VarMax, size=VarSize))[0]-1
            for k in np.arange(0, nVar):
                a = XY[k]
                League[j]["MPlayer"][i]["Position"][k] = De[int(a)]
            League[j]["MPlayer"][i]["Cost"] = CostFunction(
                League[j]["MPlayer"][i]["Position"])
        for i in np.arange(0, nReservePlayer):
            XY = np.floor(stats.uniform.rvs(
                VarMin, VarMax, size=VarSize))[0] - 1
            for k in np.arange(0, nVar):
                a = XY[k]
                League[j]["RPlayer"][i]["Position"][k] = De[int(a)]
            League[j]["RPlayer"][i]["Cost"] = CostFunction(
                League[j]["RPlayer"][i]["Position"])

    # Takhsis
    League = Takhsis(League)
    ##
    League = UpdateTotalCost(League)
    return League
