from functools import cmp_to_key

def solve(N,K,L,prefix):
    if N<L:
        return
    if L == 0:
        if K == 0:
            result.append(prefix + '$')
        return
    solve(N-1,K-array[N-1],L-1,prefix+str(array[N-1])+" ")
    solve(N-1,K,L,prefix)

def custom_sort(str1,str2):
    lst1 = list(map(int,str1[:-1].split()))
    lst2 = list(map(int,str2[:-1].split()))
    if lst1>lst2:
        return 1
    elif lst1<lst2:
        return -1
    else:
        return 0


if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        N,K = map(lambda x:int(x),input().split())
        array = [int(x) for x in input().split()]
        array.sort(reverse=True)
        result = []
        solve(N,K,4,"")
        for quadruple in sorted(set(result),key=cmp_to_key(custom_sort)):
            print(quadruple, end="")
        print()