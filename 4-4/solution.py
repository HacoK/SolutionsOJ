if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        n,h,p = [int(x) for x in input().split()]
        questions = []
        for i in range(n):
            questions.append([int(x) for x in input().split()])
        dp = [0] * (h+1)
        for i in range(questions[0][0],h+1):
            dp[i] = questions[0][1]
        for i in range(1,n):
            tmp = []
            for j in range(0,min(questions[i][0],h+1)):
                tmp.append(dp[j])
            for j in range(min(questions[i][0],h+1),h+1):
                tmp.append(max(dp[j],dp[j-questions[i][0]]+questions[i][1]))
            dp = tmp
        for i in range(h+1):
            if dp[i] >= p:
                print("YES "+str(i))
                break
        else:
            print("NO")