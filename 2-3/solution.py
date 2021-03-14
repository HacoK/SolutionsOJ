from itertools import permutations

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n, init = input().split(' ')
        n = int(n)
        vertex = input().split(' ')
        graph = {}
        visited_init = {}
        for v in vertex:
            graph[v] = []
            visited_init[v] = False
        for i in range(n):
            raw_line = input().split(' ')
            v = raw_line[0]
            raw_line = raw_line[1:]
            for i in range(n):
                if raw_line[i] == '1':
                    graph[v].append(vertex[i])

        max_depth = 0
        stacks = [[init]]
        visited_co = [visited_init]
        depths_co = [{init:1}]
        while len(stacks) != 0:
            stack = stacks.pop()
            visited = visited_co.pop()
            depths = depths_co.pop()
            max_depth = max(max_depth,max(depths.values()))
            while len(stack) > 0:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = True
                    next_v = []
                    for neighbor in graph[v]:
                        if not visited[neighbor]:
                            next_v.append(neighbor)
                            depths[neighbor] = depths[v] + 1
                    for neighbors in permutations(next_v):
                        stacks.append(stack+list(neighbors))
                        visited_co.append(visited.copy())
                        depths_co.append(depths)
                    break
        print(max_depth)