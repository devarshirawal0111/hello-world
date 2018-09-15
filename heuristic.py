from bin import *


def nextFit(itemList, binSize):
    listBin = []
    listBin.append(Bin())
    curBin = listBin[0]

    for item in itemList:
        if curBin.filled + item <= binSize:
            curBin.addItem(item)
        else:
            curBin = Bin()
            curBin.addItem(item)
            listBin.append(curBin)

    return listBin


def nextFit_dec(itemList, binSize):
    itemList.sort(reverse=True)
    return nextFit(itemList, binSize)


def firstFit(itemList, binSize):
    listBin = []
    listBin.append(Bin())

    for item in itemList:
        flag = False

        for bin in listBin:
            if bin.filled + item <= binSize:
                bin.addItem(item)
                flag = True
                break

        if flag == False:
            newBin = Bin()
            newBin.addItem(item)
            listBin.append(newBin)

    return listBin


def firstFit_dec(itemList, binSize):
    itemList.sort(reverse=True)
    return firstFit(itemList, binSize)


def firstLastFit(itemList, binSize):
    itemList.sort(reverse=True)

    listBin = []
    curBin = Bin()
    listBin.append(curBin)

    j = len(itemList) - 1
    for i in range(len(itemList)):
        curBin.addItem(itemList[i])

        while curBin.filled + itemList[j] <= binSize and i < j:
            curBin.addItem(itemList[j])
            j = j - 1

        if i >= j:
            break

        curBin = Bin()
        listBin.append(curBin)

    return listBin


def bestFit(itemList, binSize):
    listBin = []
    listBin.append(Bin())
    for item in itemList:
        minn = binSize + 1
        binInsert = []
        for bin in listBin:
            if bin.filled + item <= binSize and binSize - bin.filled < minn:
                minn = binSize - bin.filled
                binInsert = bin
        if minn == binSize + 1:
            newBin = Bin()
            newBin.addItem(item)
            listBin.append(newBin)
        else:
            binInsert.addItem(item)
    return listBin


def worstFit(itemList, binSize):
    listBin = []
    listBin.append(Bin())
    for item in itemList:
        maxx = 0
        binInsert = []
        for bin in listBin:
            if bin.filled + item <= binSize and binSize - bin.filled > maxx:
                maxx = binSize - bin.filled
                binInsert = bin
        if maxx == 0:
            newBin = Bin()
            newBin.addItem(item)
            listBin.append(newBin)
        else:
            binInsert.addItem(item)
    return listBin
