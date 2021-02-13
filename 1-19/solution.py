from queue import Queue

def solve(data):
    def partition(data,left,right):
        target = data[left]
        i = left
        j = right
        while i<j:
            while i<=right and data[i]<=target:
                i+=1
            while j>=left and data[j]>=target:
                j-=1
            if i == right+1:
                if j == left-1:
                    return
                data[left] = data[right]
                data[right] = target
                q.put((left,right-1))
                return
            elif j == left-1:
                q.put((left+1,right))
                return
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp
        tmp = data[i]
        data[i] = data[j]
        data[j] = target
        data[left] = tmp
        q.put((left,j-1))
        q.put((j+1,right))
    q = Queue()
    q.put((0,len(data)-1))
    while not q.empty():
        left,right = q.get()
        if left < right:
            partition(data,left,right)

if __name__ == "__main__":
    data = [int(x) for x in input().split()]
    num = data[0]
    data = data[1:]
    solve(data)
    print(' '.join(map(str,data)))