def solution(m, n, puddles):
    mod=1000000007
    answer = 0
    dp=[[0]*(m+1) for i in range(n+1)]
    puddles=set((x,y) for x,y in puddles)
    dp[1][1]=1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (j,i) in puddles:
                dp[i][j]=0
                continue
            if i==1 and j==1:
                continue
            else:
                dp[i][j]=(dp[i][j-1]+dp[i-1][j])%mod
    return dp[n][m]