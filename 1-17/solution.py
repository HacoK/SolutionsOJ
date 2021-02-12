def solve(data,num):
    for i in range(1,len(data)):
        for j in range(0,len(data)-i):
            if data[j]>data[j+1]:
                tmp=data[j]
                data[j]=data[j+1]
                data[j+1]=tmp

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        data = [int(x) for x in input().split()]
        num = data[0]
        # data = data[1:]
        solve(data,num)
        print(' '.join(map(str,data)))