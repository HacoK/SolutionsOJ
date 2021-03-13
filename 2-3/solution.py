def dfs(graph, visited, cur_node):
    if visited[cur_node]:
        return 0
    visited[cur_node] = True
    res = 1
    for next_node in graph[cur_node]:
        res = max(1 + dfs(graph, visited, next_node), res)
    return res


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
        res = dfs(graph, visited, start_node)
        print(res)