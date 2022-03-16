from SLCfiles.WinnerFunctionMain5 import WinnerFunctionMain5    
from SLCfiles.WinnerFunctionResrve2 import WinnerFunctionResrve2
def Imitation(League = None,Winner = None,nEval = None): 
    League,nEval = WinnerFunctionMain5(League,Winner,nEval)
    League,nEval = WinnerFunctionResrve2(League,Winner,nEval)
    return League,nEval
    
    return League,nEval