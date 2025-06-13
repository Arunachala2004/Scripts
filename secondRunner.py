if __name__ == '__main__':
    nameList = []
    markList = []
    fList = []
    for _ in range(int(input())):
        name = input()
        nameList.append(name)
        score = float(input())
        markList.append(score)
    minV = min(markList)
    idxM = [i for i, x in enumerate(markList) if x == minV]
    idxM.sort(reverse=True)
    for i in idxM:
        nameList.pop(i)
        markList.pop(i)
    minV = min(markList)
idxM = [i for i, x in enumerate(markList) if x == minV]
for j in idxM:
    fList.append(nameList[j])
    fList.sort()
for n in fList:
    print(n)   
