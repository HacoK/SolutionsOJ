if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n, init = input().split(' ')
        n = int(n)
        vertex = input().split(' ')
        graph = {}
        visited = {}
        for v in vertex:
            graph[v] = []
            visited[v] = False
        for i in range(n):
            raw_line = input().split(' ')
            v = raw_line[0]
            raw_line = raw_line[1:]
            for i in range(n):
                if raw_line[i] == '1':
                    graph[v].append(vertex[i])
        
        depth = {init:1}
        stack = [init]
        while len(stack) > 0:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                for neighbor in graph[v]:
                    stack.append(neighbor)
                    depth[neighbor] = max(depth.get(neighbor,0),depth[v]+1)
        print(max(depth.values()))