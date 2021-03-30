def find_way(x,y,cost,visited):
    global grid,res
    if x != n-1 or y != n-1:
        if x+1 < n and (x+1,y) not in visited:
            next = visited.copy()
            next.add((x+1,y))
            find_way(x+1,y,cost+grid[x+1][y],next)
        if x-1 >= 0 and (x-1,y) not in visited:
            next = visited.copy()
            next.add((x-1,y))
            find_way(x-1,y,cost+grid[x-1][y],next)
        if y+1 < n and (x,y+1) not in visited:
            next = visited.copy()
            next.add((x,y+1))
            find_way(x,y+1,cost+grid[x][y+1],next)
        if y-1 >= 0 and (x,y-1) not in visited:
            next = visited.copy()
            next.add((x,y-1))
            find_way(x,y-1,cost+grid[x][y-1],next)
    else:
        res.append(cost)
    

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        cells = [int(x) for x in input().split()]
        grid = []
        index = 0
        for i in range(n):
            line = []
            for j in range(n):
                line.append(cells[index])
                index += 1
            grid.append(line)
        res = []
        find_way(0,0,grid[0][0],set([(0,0)]))
        print(min(res))