import numpy as np
import numpy as np
from ProbabilityHost import ProbabilityHost
from Imitation import Imitation
from ProbabilityHost import ProbabilityHost
from UpdateTotalCost import UpdateTotalCost
def Competition(League = None,nEval = None): 
    global SCASettings
    nTeam = SCASettings.nTeam
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