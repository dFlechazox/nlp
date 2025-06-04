# import sys
# sys.setrecursionlimit(10000000)
def minDistance(word1, word2, Icost=1, Dcost=1, recost=1):
    if len(word1) == 0:
        return len(word2)*Icost
    elif len(word2) == 0:
        return len(word1)*Dcost
    M = len(word1)
    N = len(word2)
    output = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M + 1):
        for j in range(N + 1):
            if i == 0 and j == 0:
                output[i][j] = 0
            elif i == 0 and j != 0:
                output[i][j] = j
            elif i != 0 and j == 0:
                output[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                output[i][j] = output[i - 1][j - 1]
            else:
                output[i][j] = min(output[i - 1][j - 1] + recost, output[i - 1][j] + Icost, output[i][j - 1] + Dcost)
    return output


def backtrackingPath(word1,word2,Icost=1, Dcost=1, recost=1):
    if len(word1) == 0:
        print("MED:{}.".format(len(word2)*Icost))
        for i in range(len(word2)):
            print("insert:"+word2[i])
        return
    elif len(word2) == 0:
        print("MED:{}.".format(len(word1) * Dcost))
        for i in range(len(word1)):
            print("delete:"+word1[i])
        return
    elif word2 == word1:
        print("MED:{}.".format(0))
        return

    dp = minDistance(word1,word2,Icost=1, Dcost=1, recost=1)
    print("dp table:")
    for dpele in dp:
        print(dpele)
    m = len(dp)-1
    n = len(dp[0])-1
    print("MED:",dp[m][n])

    operation = []

    while n>=0 or m>=0:
        if n and dp[m][n-1]+Dcost == dp[m][n]:
            print("insert %c" %(word2[n-1]))
            operation.append("insert:"+word2[n-1])
            n -= 1
            continue
        if m and dp[m-1][n]+Icost == dp[m][n]:
            print("delete %c" %(word1[m-1]))
            operation.append("delete:"+word1[m-1])
            m -= 1
            continue
        if dp[m-1][n-1]+recost == dp[m][n]:
            print("replace %c %c" %(word1[m-1],word2[n-1]))
            operation.append("replace:"+word1[m - 1] + "=>"+word2[n-1])
            n -= 1
            m -= 1
            continue
        if dp[m-1][n-1] == dp[m][n]:
            operation.append("keep:"+word1[m-1])
        n -= 1
        m -= 1
    operation = operation[::-1]
    print(operation)
    return operation

def backtrackingPath1(word1,word2,Icost=1, Dcost=1, recost=1):
    if len(word1) == 0:
        print("MED:{}.".format(len(word2)*Icost))
        for i in range(len(word2)):
            print("insert:"+word2[i])
        return
    elif len(word2) == 0:
        print("MED:{}.".format(len(word1) * Dcost))
        for i in range(len(word1)):
            print("delete:"+word1[i])
        return
    elif word2 == word1:
        print("MED:{}.".format(0))
        return

    dp = minDistance(word1,word2,Icost=1, Dcost=1, recost=1)
    print("dp table:")
    for dpele in dp:
        print(dpele)
    m = len(dp)-1
    n = len(dp[0])-1
    print("MED:",dp[m][n])

    operations = backtracepath(dp,m,n,"",[],word1,word2,Dcost,Icost,recost)
    for operation in operations:
        op = operation[::-1]
        del op[-1]
        print(op)
    return operations


def backtracepath(dp,m,n,operation="",path=[],word1="",word2="",Dcost=1,Icost=1,recost=1):
    path = path + [operation]
    if m <= 0 and n <= 0:
        return [path]

    MEDpath = []

    if n == 0:
        newpaths = backtracepath(dp, m-1, n, "delete:" + word1[m - 1], path, word1, word2, Dcost, Icost, recost)
        for newpath in newpaths:
            MEDpath.append(newpath)
        return MEDpath
    if m == 0:
        newpaths = backtracepath(dp, m, n-1, "insert:"+word2[n - 1], path, word1, word2, Dcost, Icost, recost)
        for newpath in newpaths:
            MEDpath.append(newpath)
        return MEDpath
    minCost = min(dp[m][n - 1],dp[m - 1][n],dp[m - 1][n-1])

    if dp[m][n - 1] == minCost:
        if n and dp[m][n - 1] + Dcost == dp[m][n]:
            newpaths = backtracepath(dp,m,n-1,"insert:"+word2[n - 1],path,word1,word2,Dcost,Icost,recost)
            for newpath in newpaths:
                MEDpath.append(newpath)
    if dp[m-1][n] == minCost:
        if m and dp[m - 1][n] + Icost == dp[m][n]:
            newpaths = backtracepath(dp, m-1, n, "delete:" + word1[m - 1], path,word1,word2,Dcost,Icost,recost)
            for newpath in newpaths:
                MEDpath.append(newpath)
    if dp[m-1][n - 1] == minCost:
        if dp[m - 1][n - 1] + recost == dp[m][n]:
            newpaths = backtracepath(dp, m - 1, n-1, "replace:" + word1[m - 1] + "=>" + word2[n - 1], path,word1,word2,Dcost,Icost,recost)
            for newpath in newpaths:
                MEDpath.append(newpath)
        elif dp[m - 1][n - 1] == dp[m][n]:
            newpaths = backtracepath(dp, m - 1, n - 1, "keep:" + word1[m - 1], path,word1,word2,Dcost,Icost,recost)
            for newpath in newpaths:
                MEDpath.append(newpath)
    return MEDpath



if __name__ == '__main__':
    # minDistance("bcdabcdef","abcdefbcd")
    # word1 = input("输入word1:")
    # word2 = input("输入word2:")
    # Icost = input("输入插入代价:")
    # Dcost = input("输入删除代价:")
    # recost = input("输入修改代价:")
    # backtrackingPath(word1,word2,int(Icost),int(Dcost),int(recost))
    backtrackingPath1("bcdabdf", "abcdefbcd", 1, 1, 1)