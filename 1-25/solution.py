from functools import cmp_to_key


def custom_sort(pair1, pair2):
    if pair1[0] < pair2[0]:
        return -1
    elif pair1[0] == pair2[0]:
        if pair1[1] < pair2[1]:
            return -1
        elif pair1[1] == pair2[1]:
            return 0
        else:
            return 1
    else:
        return 1


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        count = int(input())
        array = [int(x) for x in input().split()]
        freq = {}
        for num in array:
            if num in freq:
                freq[num] -= 1
            else:
                freq[num] = -1
        array = [[freq.get(x), x] for x in array]
        array.sort(key=cmp_to_key(custom_sort))
        array = [str(x[1]) for x in array]
        print(' '.join(array))
