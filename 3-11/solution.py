if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        digits = [int(digit) for digit in input()]
        length = len(digits)
        queue = []
        if length%2 == 0:
            queue.append((0,length-1))
        else:
            queue.append((0,length-2))
            queue.append((1,length-1))
        result = 0
        while result == 0 and len(queue) != 0:
            r = queue.pop(0)
            if(r[0]>=r[1]):
                continue
            mid = int((r[0]+r[1])/2)
            left = sum(digits[r[0]:mid+1])
            right = sum(digits[mid+1:r[1]+1])
            if sum(digits[r[0]:mid+1]) == sum(digits[mid+1:r[1]+1]):
                result = r[1] - r[0] + 1
            else:
                if((r[0]+1,r[1]-1) not in queue):
                    queue.append((r[0]+1,r[1]-1))
                if((r[0]+2,r[1]) not in queue):
                    queue.append((r[0]+2,r[1]))
                if((r[0],r[1]-2) not in queue):
                    queue.append((r[0],r[1]-2))
        print(result)