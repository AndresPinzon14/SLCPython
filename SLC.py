# Soccer League Competition Algorithm for Discrete Problems
# Developed By: Naser Moosavian

import numpy as np
import matplotlib.pyplot as plt

from MyCost import MyCost
from SLCfiles.CreateInitialLeague import CreateInitialLeague
from SLCfiles.Competition import Competition
from SLCfiles.Thakhsis import Takhsis
import SLCfiles.ShareSettings as glob

NumberOfFunctioanEvaluations = 200000
# Problem Definition
def CostFunction(x=None): return MyCost(x)


glob.ProblemSettings["De"] = np.array([0, 1, 2, 3, 4, 5, 6])

glob.ProblemSettings["nVar"] = 200

# SLC Parameters
glob.SCASettings["nTeam"] = 10

glob.SCASettings["nMainPlayer"] = 10

glob.SCASettings["nReservePlayer"] = 10

glob.SCASettings["nTeamImport"] = 5
glob.ProblemSettings["VarMin"] = 1

glob.ProblemSettings["VarMax"] = np.asarray(glob.ProblemSettings["De"]).size

##
nEval = 0
MaxIt = 10 ** 9

VarSize = np.array([1, glob.ProblemSettings["nVar"]])

# ShareSettings
tedad = NumberOfFunctioanEvaluations
# Initialization
League = CreateInitialLeague()
# SLC Main Loop
k1 = 0
BestCost = []
for it in np.arange(1, MaxIt+1).reshape(-1):
    # Competition
    League, nEval = Competition(League, nEval)
    # Update Best Solution Ever Found
    League = Takhsis(League)
    # Update Best Cost
    BestCost.append(League(1, 1).MPlayer(1, 1).Cost)
    BestSol = League(1, 1).MPlayer(1, 1).Position
    if nEval > tedad:
        break
    # Show Iteration Information
    print(np.array(['Season ', (it), ': SuperStarPlayer = ', (BestCost(it))]))

# Results
# figure
plt.semilogy(BestCost, 'LineWidth', 2)
plt.xlabel('Number of Seasons')
plt.ylabel('Best Solution (SSP)')
