def check_chained(next,left_dict):
    global cycle
    if cycle:
        return
    else:
        if len(left_dict) == 0:
            global init
            if next == init:
                cycle = True
        else:
            if next not in left_dict.keys():
                return
            nexts = left_dict[next]
            if len(nexts) == 1:
                left_dict.pop(next)
                check_chained(nexts[0],left_dict)
            else:
                for letter in nexts:
                    next_dict = left_dict.copy()
                    list_copy = nexts.copy()
                    list_copy.remove(letter)
                    next_dict[next] = list_copy
                    check_chained(letter,next_dict)

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        N = int(input())
        str_dict = {}
        strs = input().split()
        for str in strs:
            if str[0] not in str_dict:
                str_dict[str[0]] = [str[-1]]
            else:
                str_dict[str[0]] += [str[-1]]
        cycle = False
        init = strs[0][0]
        check_chained(init,str_dict.copy())    
        if cycle:
            print(1)
        else:
            print(0)