def solve(data,num):
    for i in range(1,len(data)):
        j = i-1
        while j>=0 and data[j]>data[j+1]:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp
            j -= 1

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        data = [int(x) for x in input().split()]
        num = data[0]
        # data = data[1:]
        solve(data,num)
        print(' '.join(map(str,data)))