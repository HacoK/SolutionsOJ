from functools import cmp_to_key

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, value):
        return self.x==value.x and self.y==value.y
    def __lt__(self, value):
        return self.x<value.x or (self.x==value.x and self.y<value.y)
    
def cal_distance(p1,p2,result,min_d):
    d=(p1.x-p2.x)**2+(p1.y-p2.y)**2
    if d<min_d[0]:
        min_d[0]=d
        result.clear()
        pair=[p1,p2]
        result.append(pair)
    elif d==min_d[0]:
        pair=[p1,p2]
        result.append(pair)
    return d

def solve(points,start,end,result,min_d):
    if end==start:
        return float("inf")
    if end-start==1:
        return cal_distance(points[start],points[end],result,min_d)**0.5
    medium=int((start+end)/2)
    d1=solve(points,start,medium,result,min_d)
    d2=solve(points,medium+1,end,result,min_d)

    d=min(d1,d2)
    x=(points[medium].x+points[medium+1].x)/2
    left_border=x-d
    right_border=x+d
    i=medium
    j=medium+1
    while i>=0 and points[i].x>=left_border:
        i-=1
    if i>=0:
        i+=1
    while j<=end and points[j].x<=right_border:
        j+=1
    if j<=end:
        j-=1
    min_bet=float("inf")
    for left_p in points[i:medium+1]:
        for right_p in points[medium+1:j+1]:
            min_bet=min(min_bet,cal_distance(left_p,right_p,result,min_d))
    min_bet**=0.5
    return min(min_bet,d)

def custom_sort(pair1,pair2):
    if pair1[0]<pair2[0]:
        return -1
    elif pair1[0]==pair2[0]:
        if pair1[1]<pair2[1]:
            return -1
        elif pair1[1]==pair2[1]:
            return 0
        else:
            return 1
    else:
        return 1

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        inputs=input().split(',')
        points=[]
        for point in inputs:
            x,y = [float(x) for x in point.split()]
            points.append(Point(x,y))
        points.sort()

        result=[]
        min_d=[float("inf")]

        solve(points,0,len(points)-1,result,min_d)
        result.sort(key=cmp_to_key(custom_sort))

        result=['{:g}'.format(pair[0].x)+' '+'{:g}'.format(pair[0].y)+','+'{:g}'.format(pair[1].x)+' '+'{:g}'.format(pair[1].y) for pair in result]
        print(','.join(result))