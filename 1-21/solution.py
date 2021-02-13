def solve(num,data):
    def merge(data,fst,sec,guard):
        adder = 0
        tmp = []
        i = fst
        j = sec
        while i<sec and j<guard:
            if data[i]<=data[j]:
                tmp.append(data[i])
                i+=1
            else:
                tmp.append(data[j])
                adder+=sec-i
                j+=1
        while i<sec:
            tmp.append(data[i])
            i+=1
        while j<guard:
            tmp.append(data[j])
            j+=1
        for index in range(fst,guard):
            data[index]=tmp[index-fst]
        return adder
    counter = 0
    interval = 1
    while interval<num:
        fst = 0
        sec = interval
        while sec<num:
            counter+=merge(data,fst,sec,min(num,sec+interval))
            fst+=interval*2
            sec+=interval*2
        interval*=2
    return counter

if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        num = int(input())
        data = [int(x) for x in input().split()]
        print(solve(num,data))