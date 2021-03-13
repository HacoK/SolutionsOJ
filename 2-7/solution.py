def solve(rank):
    global ends, counts
    group = 0
    rank -= counts[group]
    while rank > 0:
        group += 1
        rank -= counts[group]
    return ends[group] + rank

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        N, Q = map(int,input().split(' '))
        start = []
        count = []
        groups = list(map(int,input().split(' ')))
        querys = list(map(int,input().split(' ')))

        starts = groups[::2]
        ends = groups[1::2]
        counts = []
        for i in range(N):
            counts.append(ends[i] - starts[i] + 1)
        scores = []
        for i in range(Q):
            scores.append(solve(querys[i]))
        print(' '.join(map(str,scores)))