import numpy as np
import scipy.stats as stats

from SLCfiles.ShareSettings import ProblemSettings, SCASettings


def ExtractCost(li):
    r = []
    for i in li:
        r.append(i[0][0]["Cost"])
    return r

def WinnerFunctionMain5(League = None,Winner = None,nEval = None): 
    
    nVar = ProblemSettings["nVar"]
    VarSize = ProblemSettings["VarSize"]
    VarMin = ProblemSettings["VarMin"]
    VarMax = ProblemSettings["VarMax"]
    De = ProblemSettings["De"]
    nMainPlayer = SCASettings["nMainPlayer"]
    nReservePlayer = SCASettings["nReservePlayer"]
    CostFunction = ProblemSettings["CostFunction"]
    for i in np.arange(0,nMainPlayer):
        A = np.random.permutation(nMainPlayer)
        print(A)
        print("x1",League[1])
        print("x2",League[1]["MPlayer"])
        print("x3",League[1]["MPlayer"][1])
        print("x4",League[0]["MPlayer"][0][0][0]["Position"])
        y1 = League[0]["MPlayer"][0][0][0]["Position"]
        y2 = League[(Winner)]["MPlayer"][0][0][0]["Position"]
        y3 = League[(Winner)]["MPlayer"][A[0]][A[1]][A[2]]["Position"]
        y4 = League[(Winner)]["MPlayer"][A[-1]][A[-2]][A[-3]]["Position"]
        x = League[(Winner)]["MPlayer"][i][0][0]["Position"]
        beta = stats.uniform.rvs(0.2,0.8,size=VarSize)
        aux1=np.array(y1) - np.array(y3)
        rq = x + np.multiply(beta,aux1)
        qqq=[None]*nVar
        for i2 in np.arange(0,nVar):
            czx=np.abs(De - rq[np.min([i2,len(rq)-1])][:len(De)]  )
            czx=np.array(list(map(int,czx)))
            print(czx)
            min = np.amin(czx)
            index=0
            for xczx in range(len(czx)):
                if(czx[xczx]==min):
                    index=xczx
            qqq[i2] = De[index]
        NewSol={}
        NewSol["Position"] = qqq
        nEval = nEval + 1
        NewSol["Cost"] = CostFunction(NewSol["Position"])
        if NewSol["Cost"] < League[(Winner)]["MPlayer"][i][0][0]["Cost"]:
            League[Winner]["MPlayer"][i][1] = NewSol
        else:
            beta = stats.uniform.rvs(0.2,0.8,VarSize)
            aux1=np.array(y2) - np.array(y3)
            rq = x + np.multiply(beta,aux1)
            for i2 in np.arange(0,nVar):

                czx=np.abs(De - rq[np.min([i2,len(rq)-1])][:len(De)]  )
                czx=np.array(list(map(int,czx)))
                print(czx)
                min = np.amin(czx)
                index=0
                for xczx in range(len(czx)):
                    if(czx[xczx]==min):
                        index=xczx
                qqq[i2] = De[index]
            NewSol["Position"] = qqq
            nEval = nEval + 1
            NewSol["Cost"] = CostFunction(NewSol["Position"])
            if NewSol["Cost"] < League[(Winner)]["MPlayer"][i][0][0]["Cost"]:
                League[Winner]["MPlayer"][i][1] = NewSol
            else:
                beta = stats.uniform.rvs(0.2,0.8,VarSize)
                aux1=np.array(y4) - np.array(y3)
                rq = x + np.multiply(beta,(aux1))
                for i2 in np.arange(0,nVar):                        
                    czx=np.abs(De - rq[np.min([i2,len(rq)-1])][:len(De)]  )
                    czx=np.array(list(map(int,czx)))
                    print(czx)
                    min = np.amin(czx)
                    index=0
                    for xczx in range(len(czx)):
                        if(czx[xczx]==min):
                            index=xczx
                    qqq[i2] = De[index]
                NewSol["Position"] = qqq
                nEval = nEval + 1
                NewSol["Cost"] = CostFunction(NewSol["Position"])
                if NewSol["Cost"] < League[(Winner)]["MPlayer"][i][1][0]["Cost"]:
                    League[Winner]["MPlayer"][i][1] = NewSol
        MainPlayer = League[(Winner)]["MPlayer"]
        Player = np.array([MainPlayer])
        PlayerCost = np.array(list(map(ExtractCost,Player)))
        a1=PlayerCost.sort(axis=1)
        SortOrder=PlayerCost.argsort(axis=1)
        Player = Player[(0)]        
        League[(Winner)]["MPlayer"] = Player[(np.arange(0,nMainPlayer))]
    
    return League,nEval
    
    return League,nEval
