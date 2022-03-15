import numpy as np
    
def Takhsis(League = None): 
    global SCASettings
    nTeam = SCASettings.nTeam
    nMainPlayer = SCASettings.nMainPlayer
    nReservePlayer = SCASettings.nReservePlayer
    for jj in np.arange(1,nTeam+1).reshape(-1):
        MainPlayer[:,jj] = League(jj,1).MPlayer
        RvrsPlayer[:,jj] = League(jj,1).RPlayer
    
    Player = np.array([[MainPlayer],[RvrsPlayer]])
    PlayerCost = np.array([Player.Cost])
    a1,SortOrder = __builtint__.sorted(PlayerCost)
    Player = Player(SortOrder)
    kk = 0
    for jj in np.arange(1,nTeam+1).reshape(-1):
        kk = kk + nMainPlayer
        League(jj,1).MPlayer = np.transpose(Player(np.arange(kk - nMainPlayer + 1,kk+1)))
        kk = kk + nReservePlayer
        League(jj,1).RPlayer = np.transpose(Player(np.arange(kk - nReservePlayer + 1,kk+1)))
    
    return League
    
    return League