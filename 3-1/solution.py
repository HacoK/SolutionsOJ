def backtracking(i1,i2,seq):
    global s1,s2,dp,result,max_length
    if len(seq) == max_length:
        result.append(seq)
        return
    if s1[i1-1] == s2[i2-1]:
        backtracking(i1-1,i2-1,s1[i1-1] + seq)
    else:
        if dp[i1-1][i2] == (max_length - len(seq)):
            backtracking(i1-1,i2,seq)
        if dp[i1][i2-1] == (max_length - len(seq)):
            backtracking(i1,i2-1,seq)

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        s1 = input()
        s2 = input()
        
        # 公共子序列最大长度
        m = len(s1)
        n = len(s2)
        dp = []
        for i in range(m+1):
            dp.append([0]*(n+1))
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        # 回溯取最长公共子序列
        result = []
        max_length = dp[m][n]
        backtracking(m,n,'')
        for seq in sorted(set(result)):
            print(seq)