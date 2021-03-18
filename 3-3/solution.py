if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        # 构造柱状图
        n,m = map(int,input().split())
        heighs = []
        pre = [0] * m
        for rid in range(n):
            heigh = []
            row = input().split()
            for pos in range(m):
                if row[pos] == '0':
                    heigh.append(0)
                else:
                    heigh.append(pre[pos] + 1)
            heighs.append(heigh)
            pre = heigh
        
        # 计算每层最大面积
        max_area = 0
        for heigh in heighs:
            stack = [0]
            for i in range(1,m):
                top = heigh[stack[-1]]
                while top > heigh[i]:
                    stack.pop()
                    if len(stack) == 0:
                        area = i * top
                        max_area = max(max_area,area)
                        break
                    else:
                        area = (i - stack[-1] - 1) * top
                        max_area = max(max_area,area)
                        top = heigh[stack[-1]]
                if top != heigh[i]:
                    stack.append(i)
            while len(stack) > 1:
                left = stack.pop()
                area = (m - stack[-1] - 1) * heigh[left]
                max_area = max(max_area,area)
            max_area = max(max_area,heigh[stack[-1]]*m)
        print(max_area)