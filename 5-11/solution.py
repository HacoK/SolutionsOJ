if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        arr = [int(x) for x in input().split()]
        n = len(arr)
        num = int(input())
        max = [0]
        min = [0]
        count = 0
        i = 0
        j = 1
        while i < n-1:
            while j < n:
                while len(max)!=0 and arr[j]>=arr[max[-1]]:
                    max.pop(-1)
                max.append(j)
                while len(min)!=0 and arr[j]<=arr[min[-1]]:
                    min.pop(-1)
                min.append(j)
                if arr[max[0]]-arr[min[0]]>num:
                    count+=n-j
                    break
                j+=1
            if max[0]==i:
                max.pop(0)
            if min[0]==i:
                min.pop(0)
            i+=1
        print(count)