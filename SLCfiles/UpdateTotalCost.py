import numpy as np

from SLCfiles.ShareSettings import SCASettings
    
def UpdateTotalCost(League = None): 
    nTeam = SCASettings["nTeam"]
    nMainPlayer = SCASettings["nMainPlayer"]
    for k in np.arange(0,nTeam):
        x=[None]*nMainPlayer
        for jj in np.arange(0,nMainPlayer):

            x[jj] = League[k]["MPlayer"][jj][0][0]["Cost"]
        League[k]["TotalCost"] = 1 / np.mean(x)
    
    return League
    
