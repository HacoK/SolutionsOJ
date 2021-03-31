def solve(coins, amounts):
    res = 0
    coins.sort(reverse=True)
    for coin in coins:
        res += amounts // coin
        amounts %= coin
        if amounts == 0:
            break
    if amounts == 0:
        print(res)
    else:
        print(-1)


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n, amounts = [int(x) for x in input().split()]
        coins = [int(x) for x in input().split()]
        solve(coins, amounts)