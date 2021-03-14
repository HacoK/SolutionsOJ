def dfs(graph, visited, cur_node, cur_depth):
    global max_depth
    max_depth = max(max_depth,cur_depth)
    visited[cur_node] = True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            dfs(graph, visited.copy(), next_node, cur_depth+1)

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n, start_node = input().split(" ")
        n = int(n)
        graph = {}
        nodes = input().split(" ")
        for node in nodes:
            graph[node] = []
        for i in range(n):
            row = input().split(" ")
            node = row[0]
            table = [int(x) for x in row[1:]]
            for idx, exist in enumerate(table):
                if exist == 1:
                    graph[node].append(nodes[idx])
        visited = {}
        for node in nodes:
            visited[node] = False
        
        max_depth = 0
        dfs(graph, visited.copy(), start_node, 1)
        print(max_depth)