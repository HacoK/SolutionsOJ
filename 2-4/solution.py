# 递归分配任务，在当前成本高于目前已知最小成本时回溯
def alloc_work(pre_alloc,cur_cost):
    global n,costM,min_cost,distri
    person = len(pre_alloc)
    if person < n:
        for i in range(n):
            if i not in pre_alloc:
                next_cost = cur_cost + costM[person][i]
                if next_cost <= min_cost:
                     alloc_work(pre_alloc+[i],next_cost)
    else:
        if cur_cost < min_cost:
            min_cost = cur_cost
            distri = [pre_alloc]
        elif cur_cost == min_cost:
            distri.append(pre_alloc)


if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        costM = []
        for i in range(n):
            costM.append([0]*n)
        for person,task,cost in [map(int,item.split(' ')) for item in input().split(',')]:
            costM[person-1][task-1] = cost
        min_cost = 0
        for i in range(n):
            min_cost += costM[i][i]
        distri = []
        alloc_work([],0)
        distri.reverse()
        print(','.join([' '.join(map(lambda x:str(x+1),res)) for res in distri]))