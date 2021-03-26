'''
C(i)为odd的情况：C(i-1)&&C(i-3)一个odd一个even
0 1 2 3 4 5 6 7 8 9 10
e e o o o e o| e e o o
'''
if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        count = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i*j)**3%7 in [2,3,4,6]:
                    count += 1
        print(count)