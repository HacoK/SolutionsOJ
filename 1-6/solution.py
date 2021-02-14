def solve(strength):
    power=0
    index=0
    while power<=strength:
        index+=1
        power+=index**2
    return index-1

if __name__ == "__main__":
    test_cnt=int(input())
    for t in range(test_cnt):
        strength=int(input())
        print(solve(strength))