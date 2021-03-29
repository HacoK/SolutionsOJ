if __name__ == "__main__":
    test_cnt = int(input())
    for t in range(test_cnt):
        N = int(input())

        brinjals = []
        carrots = []
        tomatoes= []
        for i in range(N):
            brinjal, carrot, tomato = [int(x) for x in input().split()]
            brinjals.append(brinjal)
            carrots.append(carrot)
            tomatoes.append(tomato)
        dp_brinjals = [brinjals[0]]
        dp_carrots = [carrots[0]]
        dp_tomatoes = [tomatoes[0]]
        for i in range(1,N):
            prev = i - 1
            dp_brinjals.append(min(dp_carrots[prev],dp_tomatoes[prev])+brinjals[i])
            dp_carrots.append(min(dp_brinjals[prev],dp_tomatoes[prev])+carrots[i])
            dp_tomatoes.append(min(dp_brinjals[prev],dp_carrots[prev])+tomatoes[i])
        print(min(dp_brinjals[-1],dp_carrots[-1],dp_tomatoes[-1]))