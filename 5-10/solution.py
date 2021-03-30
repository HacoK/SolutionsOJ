if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        arr = [int(x) for x in input().split()]
        w = int(input())
        sum = 0
        for i in range(0,len(arr)-(w-1)):
            sum += max(arr[i:i+w])
        print(sum)