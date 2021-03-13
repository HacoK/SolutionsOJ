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
        
        traversal = []
        queue = [init]
        while len(queue) > 0:
            v = queue.pop(0)
            if not visited[v]:
                visited[v] = True
                traversal.append(v)
                for neighbor in graph[v]:
                    queue.append(neighbor)
        
        print(' '.join(traversal))