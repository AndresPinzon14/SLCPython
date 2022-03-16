import numpy as np    
def MyCost(x = None): 
    #z=sum(-x.*sin(sqrt(abs(x))));
    x=np.array(x)
    z = np.sum( x**2)
    return z