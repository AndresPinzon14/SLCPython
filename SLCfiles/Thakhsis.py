import numpy as np

from SLCfiles.ShareSettings import SCASettings


def Takhsis(League=None):
    nTeam = SCASettings["nTeam"]
    nMainPlayer = SCASettings["nMainPlayer"]
    nReservePlayer = SCASettings["nReservePlayer"]
    MainPlayer = [None]*nTeam
    RvrsPlayer = [None]*nTeam
    for jj in np.arange(0, nTeam):
        MainPlayer[jj] = League[jj]["MPlayer"]
        RvrsPlayer[jj] = League[jj]["RPlayer"]
    
    Player = np.array(MainPlayer+RvrsPlayer)
    #print("Player:",Player[0])
    PlayerCost = np.array([Player[0]["Cost"], Player[1]["Cost"]])
    print("xXxxxxxxxxxxxxxxx:",PlayerCost)
    a1, SortOrder = sorted(PlayerCost)
    Player = Player(SortOrder)
    kk = 0
    for jj in np.arange(0, nTeam):
        kk = kk + nMainPlayer
        League[jj]["MPlayer"] = np.transpose(
            Player(np.arange(kk - nMainPlayer + 1, kk+1)))
        kk = kk + nReservePlayer
        League[jj]["RPlayer"] = np.transpose(
            Player(np.arange(kk - nReservePlayer + 1, kk+1)))

    return League
