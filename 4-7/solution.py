if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        N = int(input())
        array = [int(x) for x in input().split()]
        result = 0
        for head in range(N):
            sum = 0
            min_val = 0
            for tail in range(head,N):
                min_val = min(min_val,array[tail])
                sum += array[tail]
                result = max(result,sum-min_val)
        if result == 0:
            print(max(array))
        else:
            print(result)