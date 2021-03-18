from itertools import permutations

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        num = input()
        nums = [int(''.join(p)) for p in permutations(num)]
        nums.sort()
        nums.reverse()
        for num in nums:
            if num != 0 and num % 17 == 0:
                print(num)
                break
        else:
            print("Not Possible")