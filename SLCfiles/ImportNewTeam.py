import numpy as np
    
def ImportNewTeam(League = None,nTeamImport = None): 
    global ProblemSettings
    global SCASettings
    CostFunction = ProblemSettings.CostFunction
    nVar = ProblemSettings.nVar
    VarSize = ProblemSettings.VarSize
    VarMin = ProblemSettings.VarMin
    VarMax = ProblemSettings.VarMax
    De = ProblemSettings.De
    nTeam = SCASettings.nTeam
    nMainPlayer = SCASettings.nMainPlayer
    nReservePlayer = SCASettings.nReservePlayer
    for j in np.arange(1,nTeamImport+1).reshape(-1):
        for i in np.arange(1,nMainPlayer+1).reshape(-1):
            XY = np.round(unifrnd(VarMin,VarMax,VarSize))
            for k in np.arange(1,nVar+1).reshape(-1):
                a = XY(k)
                League[j,1].MPlayer[i,1].Position[1,k] = De(a)
            League(j,1).MPlayer(i,1).Cost = CostFunction(League(j,1).MPlayer(i,1).Position)
        for i in np.arange(1,nReservePlayer+1).reshape(-1):
            XY = np.round(unifrnd(VarMin,VarMax,VarSize))
            for k in np.arange(1,nVar+1).reshape(-1):
                a = XY(k)
                League[j,1].RPlayer[i,1].Position[1,k] = De(a)
            League(j,1).RPlayer(i,1).Cost = CostFunction(League(j,1).RPlayer(i,1).Position)
    
    ##
    
    League = UpdateTotalCost(League)
    return League
    
    return League