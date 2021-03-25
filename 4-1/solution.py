if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        R,C = [int(x) for x in input().split()]
        cells = [int(x) for x in input().split()]
        index = 0
        grid = []
        dp = []
        for row in range(R):
            grid.append([])
            dp.append([])
            for column in range(C):
                grid[row].append(cells[index])
                dp[row].append(1)
                index += 1
        if grid[R-1][C-1] < 0:
            dp[R-1][C-1] = 1-grid[R-1][C-1]
        for row in range(R-2,-1,-1):
            min_points = dp[row+1][C-1] - grid[row][C-1]
            if min_points > 1:
                dp[row][C-1] = min_points
        for col in range(C-2,-1,-1):
            min_points = dp[R-1][col+1] - grid[R-1][col]
            if min_points > 1:
                dp[R-1][col] = min_points
        for row in range(R-2,-1,-1):
            for col in range(C-2,-1,-1):
                min_points = min(dp[row][col+1],dp[row+1][col]) - grid[row][col]
                if min_points > 1:
                    dp[row][col] = min_points
        print(dp[0][0])