'''
实际上是一个数学公式题,有9个因数的数必定满足下列公式之一
x = a2 * b2
x = a8
其中a,b是质数,因此只要枚举质数即可.
'''

# 欧式筛法获得小于bound的素数列表
def find_primes(bound):
    primes = []
    checked = [False] * bound
    for num in range(2,bound):
        if not checked[num]:
            primes.append(num)
        for prime in primes:
            if num * prime >= bound:
                break
            checked[num * prime] = True
            if num % prime == 0:
                break
    return primes

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        N = int(input())
        bound = int(N**0.5)+1
        primes = find_primes(bound)
        count = 0
        for prime in primes:
            if prime ** 8 < N:
                count += 1
            else:
                break
        for i in range(len(primes)-1):
            for j in range(i+1,len(primes)):
                if primes[i] * primes[j] < bound:
                    count += 1
                else:
                    break
        print(count)