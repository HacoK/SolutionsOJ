# 1.公式法
# '''
# 利用Fibonacci递推公式：
# F[2n] = F[n+1]² - F[n-1]² = (2F[n-1] + F[n]) · F[n] ①
# F[2n+1] = F[n+1]² + F[n]² ②
# '''

# mod = int(1e9+7)
# d = {1: 1, 2: 1}

# def fib(n):
#     if n < 3:
#         return d[n]

#     if n in d:
#         return d[n]

#     if (n % 2 == 1):
#         k = (n + 1) // 2
#         x = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % mod
#         d[n] = x
#     else:
#         k = n // 2
#         x = (fib(k) * ((fib(k + 1) * 2) - fib(k))) % mod
#         d[n] = x
#     return d[n]

# for _ in range(int(input())):
#     n = int(input())
#     print(fib(n + 1))

# 2.快速幂

# import numpy as np

if __name__ == '__main__':
    test_cnt = int(input())
    mod = int(1e9 + 7)
    for t in range(test_cnt):
        N = int(input())
        # init = np.array([0,1])
        # fib = np.array([[0,1],[1,1]])
        init = [0,1]
        fib = [[0,1],[1,1]]
        while N > 0:
            if N & 1 == 1:
                # init = init @ fib % mod
                init = [(init[0]*fib[0][0]+init[1]*fib[1][0])%mod,(init[0]*fib[0][1]+init[1]*fib[1][1])%mod]
            N //= 2
            # fib = fib @ fib % mod
            fib = [[(fib[0][0]*fib[0][0]+fib[0][1]*fib[1][0])%mod,(fib[0][0]*fib[0][1]+fib[0][1]*fib[1][1])%mod],
                    [(fib[1][0]*fib[0][0]+fib[1][1]*fib[1][0])%mod,(fib[1][0]*fib[0][1]+fib[1][1]*fib[1][1])%mod]]
        print(init[-1])
        