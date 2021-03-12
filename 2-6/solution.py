def solve(A1, A2):
    head = {}
    tail = []
    for num in A1:
        if num in A2:
            head[num] = 1 if num not in head.keys() else head[num]+1
        else:
            tail.append(num)
    result = []
    for num in A2:
        if num in head.keys():
            for count in range(head[num]):
                result.append(num)
    tail.sort()
    result.extend(tail)
    return result


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        M, N = map(int,input().split(' '))
        A1 = list(map(int,input().split(' ')))
        A2 = list(map(int,input().split(' ')))
        sortedList = solve(A1, A2)
        print(' '.join(map(str,sortedList)))