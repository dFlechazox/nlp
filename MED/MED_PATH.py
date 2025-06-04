
def minDistance(word1, word2, Icost=1, Dcost=1, recost=1):
    '''

    :param word1: word1
    :param word2: word2
    :param Icost: 插入代价
    :param Dcost: 删除代价
    :param recost: 替换代价
    :return: dp table
    '''
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
                output[i][j] = j*Icost
            elif i != 0 and j == 0:
                output[i][j] = i*Dcost
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
        print("word1 与 word2 相同.")
        print("MED:{}.".format(0))
        return

    dp = minDistance(word1,word2,Icost, Dcost, recost)
    print("dp table:")
    for dpele in dp:
        print(dpele)
    m = len(dp)-1
    n = len(dp[0])-1
    print("最小编辑距离MED:{}.".format(dp[m][n]))

    operations = backtracepath(dp,m,n,"",[],word1,word2,Dcost,Icost,recost)
    print("总共{}条最小编辑路径.[insert表示在当前位置插入，keep表示不变，delete表示删除，replace表示替换]".format(len(operations)))
    for operation in operations:
        op = operation[::-1]
        del op[-1]
        print(op)
    return operations


def backtracepath(dp,m,n,operation="",path=[],word1="",word2="",Dcost=1,Icost=1,recost=1):
    path = path + [operation]
    if m <= 0 and n <= 0:
        return [path]

    MEDpath = [] # 存储总路径

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
    print("该程序计算word1转换为word2的最小编辑距离及编辑路径！")
    word1 = input("输入word1[默认为bcdabcdef]:") or "bcdabcdef"
    word2 = input("输入word2[默认为abcdefbcd]:") or "abcdefbcd"
    Icost = eval(input("输入插入代价:"))
    Dcost = eval(input("输入删除代价:"))
    recost = eval(input("输入替换代价:"))
    backtrackingPath(word1,word2,Icost,Dcost,recost)
    # backtrackingPath("bcdabcdef", "abcdefbcd", 1.5, 1.5, 1.5)
    input("按回车键退出...")