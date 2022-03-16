import numpy as np

from SLCfiles.ShareSettings import SCASettings


def ExtractCost(li):
    r = []
    for i in li:
        r.append(i["Cost"])
    return r


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
    print("n", nTeam, "x", len(Player))
    # print(Player[0][0])
    PlayerCost = np.array(list(map(ExtractCost, Player)))
    a1=PlayerCost.sort(axis=1)
    SortOrder=PlayerCost.argsort(axis=1)
    Player = Player[SortOrder]
    kk = 0
    for jj in np.arange(0, nTeam):
        kk = nMainPlayer
        League[jj]["MPlayer"] = np.transpose(
            Player[np.arange(0 , kk)])
        kk = nReservePlayer
        League[jj]["RPlayer"] = np.transpose(
            Player[np.arange(0, kk)])

    return League
