import math

def solve(BT):
    num=len(BT)
    layer=math.ceil(math.log(num,2))
    for i in range(layer):
        start=2**i
        end=min(num,2**(i+1))
        print(' '.join(map(str,sorted(set(BT[start:end])))))

if __name__ == '__main__':
    test_cnt=int(input())
    for t in range(test_cnt):
        num=int(input())
        BT=[int(x) for x in input().split()]
        BT.insert(0,0)
        solve(BT)