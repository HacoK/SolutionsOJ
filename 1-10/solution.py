# 递归
def solve_1(n,m):
    if n < m:
        return -1
    if m==1:
        return sum(pages[0:n])
    tmp = []
    for i in range(1,n-m+2):
        tmp.append(max(solve_1(n-i,m-1),sum(pages[n-i:n])))
    return min(tmp)

# DP
def solve_2(n,m):
    if n < m:
        return -1
    dp = [sum(pages[0:i]) for i in range(1,(n-m+2))]
    last_layer = []
    for layer in range(2,m):
        last_layer = dp
        dp = []
        for i in range(0,n-m+1):# index cur_layer
            num = layer + i
            tmp = []
            for j in range(0,i+1):# index last_layer
                count = i - j + 1
                tmp.append(max(last_layer[j],sum(pages[num-count:num])))
            dp.append(min(tmp))
    tmp = []
    for i in range(m-1,n):
        index_dp = i-(m-1)
        tmp.append(max(dp[index_dp],sum(pages[-(n-i):])))
    return min(tmp)

# 二分查找
def solve_3(n,m):
    if n < m:
        return -1
    min_cap = max(pages)
    max_cap = sum(pages)
    if n==m:
        return min_cap
    def cal_num(capacity):
        count = 1
        cur_cap = capacity
        for page in pages:
            if(page<=cur_cap):
                cur_cap-=page
            else:
                count+=1
                cur_cap = capacity-page
        return count
    while min_cap<=max_cap:
        medium = int((min_cap+max_cap)/2)
        num = cal_num(medium)
        if num<m:
            max_cap = medium-1
        elif num>m:
            min_cap = medium+1
        else:
            if cal_num(medium-1)==m:
                max_cap = medium-1
            else:
                return medium

if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n = int(input())
        pages = [int(x) for x in input().split()]
        m = int(input())
        print(solve_3(n, m))