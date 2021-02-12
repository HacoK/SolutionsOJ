def solve(N,array):
    count = 0
    origin = array.copy()
    array.sort()
    swap_vals = []
    for i in range(N):
        if origin[i]!=array[i]:
            swap_vals.append(origin[i])
    while len(swap_vals)>0:
        val = swap_vals.pop()
        src = origin.index(val)
        dst = array.index(val)
        if src!=dst:
            tmp = origin[src]
            origin[src] = origin[dst]
            origin[dst] =tmp
            count+=1
    return count

if __name__ == "__main__":
    test_cnt = int(input())
    try:
        while(input()):
            array = [int(x) for x in input().split()]
            print(solve(len(array),array))
    except:
        pass