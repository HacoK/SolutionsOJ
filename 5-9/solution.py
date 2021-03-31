if __name__ == "__main__":
    for _ in range(int(input())):
        arr = [int(x) for x in input().split()]
        sum = int(input())
        num_dict = {}
        for num in arr:
            num_dict[num] = num_dict.get(num,0) + 1
        pairs = 0
        if num % 2 == 0:
            count = num_dict.get(num//2,0)
            pairs += count*(count-1)
            num_dict.pop(num//2,0)
        for num in arr:
            pairs += num_dict.get(sum-num,0)
        pairs //= 2
        print(pairs)