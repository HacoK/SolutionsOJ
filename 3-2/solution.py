import heapq

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        array = [int(x) for x in input().split()]
        L,R = map(int,input().split())
        K = int(input())
        array = array[L-1:R]
        heapq.heapify(array)
        print(heapq.nsmallest(K,array)[-1])