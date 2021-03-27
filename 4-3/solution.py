def findMaxSum(pos,left,pre):
    global N
    if pos == N:
        global max_sum
        if pre > max_sum:
            max_sum = pre
    else:
        global elements
        e = elements[pos]
        add = True
        for digit in e:
            if digit not in left:
                add = False
                break
        if add:
            left_add = left.copy()
            for digit in e:
                if digit in left_add:
                    left_add.remove(digit)
            findMaxSum(pos+1,left_add,pre+int(e))
        findMaxSum(pos+1,left,pre)


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        N = int(input())
        elements = input().split()
        # for e in elements:
        #     exist = []
        #     duplicate = False
        #     for d in e:
        #         if d in exist:
        #             duplicate = True
        #             break
        #         else:
        #             exist.append(d)
        #     if duplicate:
        #         elements.remove(e)
        # N = len(elements)
        max_sum = 0
        digits = ['0','1','2','3','4','5','6','7','8','9']
        findMaxSum(0,digits,0)
        print(max_sum)