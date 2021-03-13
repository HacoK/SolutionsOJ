'''
Don't know why there's runtime error
'''

# def findForceZero(M):
#     result = []
#     for i in range(len(M)-1):
#         left = M[i]
#         right = M[i+1]
#         while right-left > 0.0000000000001:
#             mid = (left + right) / 2
#             force = sum(map(lambda pos:1/(mid-pos),M))
#             if force < 0:
#                 right = mid
#             elif force > 0:
#                 left = mid
#             else:
#                 break
#         result.append("{:.2f}".format(mid))
#     return result

# if __name__ == '__main__':
#     test_cnt = int(input())
#     for t in range(test_cnt):
#         N = int(input())
#         M = list(map(int,input().split(' ')))
#         result = findForceZero(M)
#         print(' '.join(result))

def solve(positions):
    n = len(positions)
    distances = [0] * n
    for i in range(1, n):
        distances[i] = distances[i-1] + positions[i] - positions[i-1]
    res = []
    for i in range(n-1):
        p = 0
        q = positions[i+1] - positions[i]
        mid = p + (q - p) / 2
        found = False
        while q - p > 0.0000000000001:
            mid = p + (q - p) / 2
            left = 0
            right = 0
            for j in range(i+1):
                left += 1 / (distances[i] - distances[j] + mid)
            for j in range(i+1, n):
                right += 1 / (distances[j] - distances[i+1] + positions[i+1] - positions[i] - mid)
            if left < right:
                q = mid
            elif left > right:
                p = mid
            else:
                found = True
                res.append(positions[i] + mid)
                break
        if not found:
            res.append(positions[i] + mid)
    print(" ".join(["%.2f" % x for x in res]))


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        positions = [int(x) for x in input().split()]
        solve(positions)