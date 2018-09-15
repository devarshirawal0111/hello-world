from heuristic import *


def showBin(listBin):
    listItems = []

    for bin in listBin:
        listItems.append(bin.show())

    return listItems


def showFilled(listBin):
    list = []

    for bin in listBin:
        list.append(bin.filled)

    return list


def main():
    num_array = []

    print("Enter the number of values you want to enter: \n")
    n = int(input())

    print("Enter the values:\n")
    for i in range(n):
        a = int(input())
        num_array.append(a)

    print("Enter the size of bin:\n")
    binSize = int(input())

    ans = showBin(firstLastFit(num_array, binSize))
    for i in ans:
        print(*i)

    return showFilled(firstLastFit(num_array, binSize))


if __name__ == "__main__":
    main()
