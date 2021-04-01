if __name__ == '__main__':
    for _ in range(int(input())):
        n,p = [int(x) for x in input().split()]
        matrix = []
        for i in range(n+1):
            matrix.append([0]*(n+1))
        for i in range(p):
            edge = [int(x) for x in input().split()]
            matrix[edge[0]][edge[1]] = edge[2]
        tank = []
        tap = []
        min_diameter = []
        for i in range(1,n+1):
            inner = max([matrix[x][i] for x in range(1,n+1)])
            if inner == 0:
                tank.append(i)
        for start in tank:
            cur_house = start
            diameters = []
            while True:
                diameter = max(matrix[cur_house])
                if diameter == 0:
                    tap.append(cur_house)
                    break
                diameters.append(diameter)
                cur_house = matrix[cur_house].index(diameter)
            min_diameter.append(min(diameters))
        pairs = n - p
        print(pairs)
        for i in range(pairs):
            print(tank[i],tap[i],min_diameter[i])