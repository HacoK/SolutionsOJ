if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        text,pattern = input().split(',')
        result = []
        for i in range(len(text)-len(pattern)+1):
            if text[i] == pattern[0]:
                for k in range(1,len(pattern)):
                    if text[i+k] != pattern[k]:
                        break
                else:
                    result.append(str(i))
        print(' '.join(result))