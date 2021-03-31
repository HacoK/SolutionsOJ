if __name__ == "__main__":
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        N = len(a)
        c = a + b
        min_val = min(c)
        c = list(map(lambda x:x-min_val,c))
        sum_c = sum(c)
        benchmark = sum_c//2
        flag = []
        for i in range(N+1):
            flag.append([])
            for j in range(benchmark+1):
                flag[i].append(False)
        flag[0][0] = True
        for k in range(2*N):
            for i in range(N if k+1>N else k+1,0,-1):
                for j in range(benchmark+1):
                    if c[k] <= j and flag[i-1][j-c[k]]:
                        flag[i][j] = True
        for point in range(benchmark,-1,-1):
            if flag[N][point]:
                print(sum_c-2*point)
                break