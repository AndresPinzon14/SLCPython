import numpy as np

def ProbabilityHost(League = None,ii = None,jj = None): 
    Psimple = (League[ii]["TotalCost"]) / (League[ii]["TotalCost"] + League[jj]["TotalCost"])
    Phost = Psimple
    if np.random.uniform() < Phost:
        Winner = ii
        Loser = jj
    else:
        Winner = jj
        Loser = ii
    
    return Winner,Loser
    
    return Winner,Loser