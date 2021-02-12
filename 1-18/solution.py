def solve(data):
    num = len(data)
    counter = []
    for i in range(0,num):
        counter.append(0)
    for i in range(0,num-1):
        for j in range(i+1,num):
            if data[i]>data[j]:
                counter[i]+=1
            else:
                counter[j]+=1
    return [data[counter.index(rank)] for rank in range(0,num)]


if __name__ == '__main__':
    try:
        while True:
            data = list(map(int, input().strip().split(' ')))
            num = data[0]
            data = data[1:]
            print(' '.join(map(str,solve(data))))
    except EOFError:
        pass