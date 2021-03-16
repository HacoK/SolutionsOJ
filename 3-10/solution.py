if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        N,M = map(int,input().split())
        array = [int(element) for element in input().split()]
        queries = [int(query) for query in input().split()]
        result = []
        for query in queries:
            count = 0
            for element in array:
                if element % query == 0:
                    count += 1
            result.append(count)
        print(' '.join(map(str,result)))