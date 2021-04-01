if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arrive = [int(x) for x in input().split()]
        depart = [int(x) for x in input().split()]
        arrive.sort()
        depart.sort()
        cur_num = 0
        platforms =0
        while len(arrive) != 0:
            if arrive[0] < depart[0]:
                arrive.pop(0)
                cur_num += 1
                platforms = max(platforms,cur_num)
            elif arrive[0] > depart[0]:
                depart.pop(0)
                cur_num -= 1
            else:
                arrive.pop(0)
                depart.pop(0)
        print(platforms)