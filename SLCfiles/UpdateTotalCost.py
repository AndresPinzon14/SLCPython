import numpy as np

from SLCfiles.ShareSettings import SCASettings
    
def UpdateTotalCost(League = None): 
    nTeam = SCASettings["nTeam"]
    nMainPlayer = SCASettings["nMainPlayer"]
    for k in np.arange(1,nTeam+1).reshape(-1):
        x=[None]*nMainPlayer
        for jj in np.arange(1,nMainPlayer+1).reshape(-1):
            x[jj] = League(k,1).MPlayer(jj,1).Cost
        League(k).TotalCost = 1 / np.mean(x)
    
    return League
    