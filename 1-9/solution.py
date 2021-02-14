def solve(points):
    def orientation(p1,p2,judge):
        return (judge[1]-p2[1])*(p2[0]-p1[0])-(p2[1]-p1[1])*(judge[0]-p2[0])
    hull = []
    for point in points:
        while len(hull)>=2 and orientation(hull[-2],hull[-1],point)>0:
            hull.pop()
        hull.append(point)
    for point in reversed(points):
        while len(hull)>=2 and orientation(hull[-2],hull[-1],point)>0:
            hull.pop()
        hull.append(point)
    hull=list(set(hull))
    hull.sort()
    if len(hull)<3:
        print(-1)
        return
    print(', '.join([str(t[0])+' '+str(t[1]) for t in hull]))

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        num = int(input())
        data = [int(x) for x in input().split()]
        points = list(zip(data[::2],data[1::2]))
        points.sort()
        solve(points)