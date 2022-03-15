import numpy as np
    
def WinnerFunctionResrve2(League = None,Winner = None,nEval = None): 
    global De
    global ProblemSettings
    global SCASettings
    nVar = ProblemSettings.nVar
    VarSize = ProblemSettings.VarSize
    VarMin = ProblemSettings.VarMin
    VarMax = ProblemSettings.VarMax
    nMainPlayer = SCASettings.nMainPlayer
    nReservePlayer = SCASettings.nReservePlayer
    CostFunction = ProblemSettings.CostFunction
    for i in np.arange(1,np.rint(nReservePlayer / 1)+1).reshape(-1):
        xxx = 0
        a = randperm(nMainPlayer)
        Gravity = League(Winner,1).MPlayer(a(end() - 1),1).Position
        x = League(Winner,1).RPlayer(end(),1).Position
        beta = unifrnd(0.9,1.1,VarSize)
        rq = np.amin(np.amax(Gravity + (np.multiply(beta,(Gravity - x))),np.amin(De)),np.amax(De))
        for i2 in np.arange(1,nVar+1).reshape(-1):
            __,index = np.amin(np.abs(De - rq(i2)))
            NewSol.Position[1,i2] = De(index)
        nEval = nEval + 1
        NewSol.Cost = CostFunction(NewSol.Position)
        if NewSol.Cost < League(Winner,1).RPlayer(end(),1).Cost:
            League[Winner,1].RPlayer[end(),1] = NewSol
        else:
            beta = unifrnd(0.4,0.6,VarSize)
            rq = np.amin(np.amax(Gravity + (np.multiply(beta,(x - Gravity))),np.amin(De)),np.amax(De))
            for i2 in np.arange(1,nVar+1).reshape(-1):
                __,index = np.amin(np.abs(De - rq(i2)))
                NewSol.Position[1,i2] = De(index)
            nEval = nEval + 1
            NewSol.Cost = CostFunction(NewSol.Position)
            if NewSol.Cost < League(Winner,1).RPlayer(end(),1).Cost:
                League[Winner,1].RPlayer[end(),1] = NewSol
            else:
                XY = np.round(unifrnd(VarMin,VarMax,VarSize))
                for k in np.arange(1,nVar+1).reshape(-1):
                    a = XY(k)
                    zz.Position[1,k] = De(a)
                nEval = nEval + 1
                zz.Cost = CostFunction(zz.Position)
                League[Winner,1].RPlayer[end(),1] = zz
        MainPlayer = League(Winner,1).MPlayer
        RvrsPlayer = League(Winner,1).RPlayer
        Player = np.array([[MainPlayer],[RvrsPlayer]])
        PlayerCost = np.array([Player.Cost])
        a1,SortOrder = __builtint__.sorted(PlayerCost)
        Player = Player(SortOrder)
        League(Winner,1).MPlayer = Player(np.arange(1,nMainPlayer+1))
        League(Winner,1).RPlayer = Player(np.arange(nMainPlayer + 1,nMainPlayer + nReservePlayer+1))
    
    return League,nEval
    
    return League,nEval