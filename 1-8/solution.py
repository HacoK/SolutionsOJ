def solve(a, b, c):
    a = a % c
    ret = a
    for i in range(b-1):
        ret *= a
        ret %= c
    return ret

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        a, b, c = [int(x) for x in input().split()]
        print(solve(a, b, c))