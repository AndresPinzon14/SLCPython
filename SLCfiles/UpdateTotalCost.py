import numpy as np
    
def UpdateTotalCost(League = None): 
    global SCASettings
    nTeam = SCASettings.nTeam
    nMainPlayer = SCASettings.nMainPlayer
    for k in np.arange(1,nTeam+1).reshape(-1):
        for jj in np.arange(1,nMainPlayer+1).reshape(-1):
            x[jj] = League(k,1).MPlayer(jj,1).Cost
        League(k).TotalCost = 1 / mean(x)
    
    return League
    
    return League