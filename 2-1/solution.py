def solve(graph,removed_v):
    if len(removed_v) == len(graph):
        global count
        count += 1
    else:
        degrees = {}
        for v in graph.keys():
            if v not in removed_v:
                degrees[v] = 0
        for inVertex,outList in graph.items():
            if inVertex not in removed_v:
                for outVertex in outList:
                    degrees[outVertex] += 1
        zero_degree = []
        for vertex,degree in degrees.items():
            if degree==0:
                zero_degree.append(vertex)
        for v in zero_degree:
            solve(graph,removed_v+[v])

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        count = 0
        raw_edges = input().split(',')
        graph = {}
        removed_v = []
        for edge in raw_edges:
            x,y = edge.split(' ')
            if x not in graph.keys():
                graph[x] = [y]
            else:
                graph[x].append(y)
            if y not in graph.keys():
                graph[y] = []
        solve(graph,removed_v)
        print(count)