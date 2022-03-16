import numpy as np
import numpy as np
from SLCfiles.Imitation import Imitation
from SLCfiles.ProbabilityHost import ProbabilityHost
from SLCfiles.UpdateTotalCost import UpdateTotalCost
import SLCfiles.ShareSettings as glob
def Competition(League = None,nEval = None): 
    nTeam = glob.SCASettings["nTeam"]
    for ii in np.arange(1,nTeam - 2+1).reshape(-1):
        for jj in np.arange(ii + 1,nTeam+1).reshape(-1):
            Winner,Loser = ProbabilityHost(League,ii,jj)
            League,nEval = Imitation(League,Winner,nEval)
            if np.random.uniform() < 0.01:
                a = np.random.permutation(range(nTeam))
                x = League(a(1),1).RPlayer(1,1)
                y = League(a(2),1).RPlayer(1,1)
                League[a[1],1].RPlayer[1,1] = y
                League[a[2],1].RPlayer[1,1] = x
            League = UpdateTotalCost(League)
    
    return League,nEval