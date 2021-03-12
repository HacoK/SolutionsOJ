def solve(painter,board,boards):
    if board <= painter:
        return max(boards)
    dp = [sum(boards[0:cnt]) for cnt in range(1,board-painter+2)]
    for painterCnt in range(2,painter+1):
        dp_next = []
        for endPoint in range(painterCnt,board-painter+painterCnt+1): #不包含endPoint
            tmp = []
            for interupt in range(painterCnt-1,endPoint):
                tmp.append(max(sum(boards[interupt:endPoint]),dp[interupt-(painterCnt-1)]))
            dp_next.append(min(tmp))
        dp = dp_next
    return dp[-1]

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        painter,board = map(int,input().split(' '))
        boards = list(map(int,input().split(' ')))
        min_time = solve(painter,board,boards)
        print(min_time)