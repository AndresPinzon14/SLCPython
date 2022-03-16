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
    for j in np.arange(1,nTeam+1).reshape(-1):
        for i in np.arange(1,nMainPlayer+1).reshape(-1):
            XY = np.round(stats.uniform.rvs(VarMin,VarMax,size=VarSize))
            for k in np.arange(1,nVar+1).reshape(-1):
                a = XY(k)
                League[j,1].MPlayer[i,1].Position[1,k] = De(a)
            League(j,1).MPlayer(i,1).Cost = CostFunction(League(j,1).MPlayer(i,1).Position)
        for i in np.arange(1,nReservePlayer+1).reshape(-1):
            XY = np.round(stats.uniform.rvs(VarMin,VarMax,size=VarSize))
            for k in np.arange(1,nVar+1).reshape(-1):
                a = XY(k)
                League[j,1].RPlayer[i,1].Position[1,k] = De(a)
            League(j,1).RPlayer(i,1).Cost = CostFunction(League(j,1).RPlayer(i,1).Position)
    
    ## Takhsis
    League = Takhsis(League)
    ##
    League = UpdateTotalCost(League)
    return League
    