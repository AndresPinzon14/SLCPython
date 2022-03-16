## Soccer League Competition Algorithm for Discrete Problems
## Developed By: Naser Moosavian

import numpy as np
import matplotlib.pyplot as plt

from MyCost import MyCost
from SLCfiles.CreateInitialLeague import CreateInitialLeague
global De,nVar
NumberOfFunctioanEvaluations = 200000
## Problem Definition
CostFunction = lambda x = None: MyCost(x)

De = np.array([0,1,2,3,4,5,6])

nVar = 200

## SLC Parameters
nTeam = 10

nMainPlayer = 10

nReservePlayer = 10

nTeamImport = 5
VarMin = 1

VarMax = np.asarray(De).size

##
nEval = 0
MaxIt = 10 ** 9

VarSize = np.array([1,nVar])

##ShareSettings
tedad = NumberOfFunctioanEvaluations
## Initialization
League = CreateInitialLeague()
## SLC Main Loop
k1 = 0
for it in np.arange(1,MaxIt+1).reshape(-1):
    ## Competition
    League,nEval = Competition(League,nEval)
    # Update Best Solution Ever Found
    League = Takhsis(League)
    # Update Best Cost
    BestCost[it] = League(1,1).MPlayer(1,1).Cost
    BestSol = League(1,1).MPlayer(1,1).Position
    if nEval > tedad:
        break
    # Show Iteration Information
    print(np.array(['Season ',num2str(it),': SuperStarPlayer = ',num2str(BestCost(it))]))

## Results
figure
semilogy(BestCost,'LineWidth',2)
plt.xlabel('Number of Seasons')
plt.ylabel('Best Solution (SSP)')