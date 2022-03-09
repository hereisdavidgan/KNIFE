while True:
    try:
        s1 = input()
        s2 = input()

        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        for i in range(len(s1) + 1):
            dp[0][i] = i

        for j in range(len(s2) + 1):
            dp[j][0] = j

        for i in range(1, len(s2) + 1):

            for j in range(1, len(s1) + 1):

                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                print(dp)
        print(dp[len(s2)][len(s1)])

    except:
        break
