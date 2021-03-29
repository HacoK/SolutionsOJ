if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        array = [int(x) for x in input().split()]
        sum = 0
        array.sort()
        while len(array) != 0:
            num = array[-1]
            sum += num
            index = array.index(num)
            array.pop(-1)
            if index!=0 and array[index-1] == num-1:
                array.pop(index-1)
        print(sum)