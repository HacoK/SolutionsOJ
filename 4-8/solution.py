if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        N,X,Y = [int(x) for x in input().split()]
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]

        tips = 0
        differs = [(A[i]-B[i],i) for i in range(N)]
        differs.sort(key=lambda x:x[0],reverse=True)
        a,b = 0,0
        while a < min(X,N) and differs[a][0] >= 0:
            tips += A[differs[a][1]]
            a += 1
        while b < min(Y,N-a) and differs[-1-b][0] <= 0:
            tips += B[differs[-1-b][1]]
            b += 1
        if a+b < N:
            if a == X:
                for i in range(a,N-b):
                    tips += A[differs[i][1]]
            else:
                for i in range(a,N-b):
                    tips += B[differs[i][1]]
        print(tips)