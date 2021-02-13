def solve(array,interval):
    for start in range(0,interval):
        for i in range(start+interval,len(array),interval):
            j = i-interval
            while j>=0 and array[j]>array[j+interval]:
                tmp = array[j]
                array[j] = array[j+interval]
                array[j+interval] = tmp
                j -= interval

if __name__ == '__main__':
    test_cnt=int(input())
    for t in range(test_cnt):
        array = [int(x) for x in input().split()]
        intervals = [int(x) for x in input().split()]
        for interval in intervals:
            solve(array,interval)
        print(' '.join(map(str,array)))