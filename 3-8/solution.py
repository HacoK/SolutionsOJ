if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        count = 0
        N = int(input())
        x_dict = {}
        y_dict = {}
        for i in range(N):
            x,y = map(int,input().split())
            if x in x_dict.keys():
                x_dict[x].add(y)
            else:
                x_dict[x] = set([y])
            if y in y_dict.keys():
                y_dict[y].add(x)
            else:
                y_dict[y] = set([x])
        for y_set in x_dict.values():
            length = len(y_set)
            count += length * (length-1) // 2
        for x_set in y_dict.values():
            length = len(x_set)
            count += length * (length-1) // 2
        print(count)