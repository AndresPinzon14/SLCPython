import numpy as np
    
def WinnerFunctionMain5(League = None,Winner = None,nEval = None): 
    global De
    global ProblemSettings
    global SCASettings
    nVar = ProblemSettings.nVar
    VarSize = ProblemSettings.VarSize
    VarMin = ProblemSettings.VarMin
    VarMax = ProblemSettings.VarMax
    De = ProblemSettings.De
    nMainPlayer = SCASettings.nMainPlayer
    nReservePlayer = SCASettings.nReservePlayer
    CostFunction = ProblemSettings.CostFunction
    for i in np.arange(1,nMainPlayer+1).reshape(-1):
        A = randperm(nMainPlayer)
        A[A == i] = []
        y1 = League(1,1).MPlayer(1,1).Position
        y2 = League(Winner,1).MPlayer(1,1).Position
        y3 = League(Winner,1).MPlayer(A(end()),1).Position
        y4 = League(Winner,1).MPlayer(A(end() - 1),1).Position
        x = League(Winner,1).MPlayer(i,1).Position
        beta = unifrnd(0.2,0.8,VarSize)
        rq = x + np.multiply(beta,(y1 - y3))
        for i2 in np.arange(1,nVar+1).reshape(-1):
            __,index = np.amin(np.abs(De - rq(i2)))
            qqq[1,i2] = De(index)
        NewSol.Position = qqq
        nEval = nEval + 1
        NewSol.Cost = CostFunction(NewSol.Position)
        if NewSol.Cost < League(Winner,1).MPlayer(i,1).Cost:
            League[Winner,1].MPlayer[i,1] = NewSol
        else:
            beta = unifrnd(0.2,0.8,VarSize)
            rq = x + np.multiply(beta,(y2 - y3))
            for i2 in np.arange(1,nVar+1).reshape(-1):
                __,index = np.amin(np.abs(De - rq(i2)))
                qqq[1,i2] = De(index)
            NewSol.Position = qqq
            nEval = nEval + 1
            NewSol.Cost = CostFunction(NewSol.Position)
            if NewSol.Cost < League(Winner,1).MPlayer(i,1).Cost:
                League[Winner,1].MPlayer[i,1] = NewSol
            else:
                beta = unifrnd(0.2,0.8,VarSize)
                rq = x + np.multiply(beta,(y4 - y3))
                for i2 in np.arange(1,nVar+1).reshape(-1):
                    __,index = np.amin(np.abs(De - rq(i2)))
                    qqq[1,i2] = De(index)
                NewSol.Position = qqq
                nEval = nEval + 1
                NewSol.Cost = CostFunction(NewSol.Position)
                if NewSol.Cost < League(Winner,1).MPlayer(i,1).Cost:
                    League[Winner,1].MPlayer[i,1] = NewSol
        MainPlayer = League(Winner,1).MPlayer
        Player = np.array([MainPlayer])
        PlayerCost = np.array([Player.Cost])
        a1,SortOrder = __builtint__.sorted(PlayerCost)
        Player = Player(SortOrder)
        League(Winner,1).MPlayer = Player(np.arange(1,nMainPlayer+1))
    
    return League,nEval
    
    return League,nEval