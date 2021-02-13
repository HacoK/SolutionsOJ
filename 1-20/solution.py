def solve(num,data):
    def merge(data,fst,sec,guard):
        tmp = []
        i = fst
        j = sec
        while i<sec and j<guard:
            if data[i]<data[j]:
                tmp.append(data[i])
                i+=1
            else:
                tmp.append(data[j])
                j+=1
        while i<sec:
            tmp.append(data[i])
            i+=1
        while j<guard:
            tmp.append(data[j])
            j+=1
        for index in range(fst,guard):
            data[index]=tmp[index-fst]
    interval = 1
    while interval<num:
        fst = 0
        sec = interval
        while sec<num:
            merge(data,fst,sec,min(num,sec+interval))
            fst+=interval*2
            sec+=interval*2
        interval*=2

if __name__ == "__main__":
    data = [int(x) for x in input().split()]
    num = data[0]
    data = data[1:]
    solve(num,data)
    print(' '.join(map(str,data)))