if __name__ == "__main__":
    for _ in range(int(input())):
        N,M = [int(x) for x in input().split()]
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]
        p,q,result = 0,0,0
        sumA,sumB = 0,0
        while p < N and q < M:
            if A[p] < B[q]:
                sumA += A[p]
                p += 1
            elif A[p] > B[q]:
                sumB += B[q]
                q += 1
            else:
                result += max(sumA,sumB) + A[p]
                sumA,sumB = 0,0
                p,q = p+1,q+1
        sumA += sum(A[p:N])
        sumB += sum(B[q:M])
        result += max(sumA,sumB)
        print(result)