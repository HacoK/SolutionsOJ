if __name__ == '__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        alphabet = [False]*26
        for x in input():
            alphabet[ord(x)-ord('A')] = True
        max_length = 0
        max_charsum = 0
        difference = 0
        result = ''
        for i in range(len(alphabet)):
            if alphabet[i]:
                k = 1
                while i+k<len(alphabet):
                    str = chr(i+ord('A'))
                    cur_length = 1
                    init = i + k
                    while init<len(alphabet) and alphabet[init]:
                        cur_length += 1
                        str = chr(init+ord('A')) + str
                        init += k
                    if cur_length > max_length:
                        max_length = cur_length
                        max_charsum = ord(str[0]) + ord(str[-1])
                        difference = k
                        result = str
                    elif cur_length == max_length:
                        if ord(str[0]) + ord(str[-1]) > max_charsum:
                            max_charsum = ord(str[0]) + ord(str[-1])
                            difference = k
                            result = str
                        elif ord(str[0]) + ord(str[-1]) == max_charsum:
                            if k < difference:
                                difference = k
                                result = str
                    k += 1
        print(result)


# My General Solution:

# from itertools import combinations

# if __name__ == '__main__':
#     test_cnt = int(input())
#     for t in range(test_cnt):
#         chars = [x for x in input()]
#         chars = list(set(chars))
#         chars.sort()
#         chars.reverse()
#         if len(chars)==1:
#             print(chars[0])
#         else:
#             pairs = combinations(chars,2)
#             # 构建距离相等的字母对
#             intervals = {}
#             for pair in pairs:
#                 distance = ord(pair[0]) - ord(pair[1])
#                 if distance in intervals.keys():
#                     intervals[distance].append(pair)
#                 else:
#                     intervals[distance] = [pair]
#             max_length = 0
#             max_charsum = 0
#             difference = 0
#             result = ''
#             for distance in intervals.keys():
#                 interval = intervals[distance]
#                 mergeMap = {}
#                 # 连接距离相等的字母对得到字符串
#                 for pair in interval:
#                     if pair[0] not in mergeMap.keys():
#                         mergeMap[pair[1]] = pair[0] + pair[1]
#                     else:
#                         prefix = mergeMap.pop(pair[0])
#                         mergeMap[pair[1]] = prefix + pair[1]
#                 # 与当前最佳字符串比较长度，ascii和以及公差，确定最佳字符串
#                 for str in mergeMap.values():
#                     if len(str) > max_length:
#                         max_length = len(str)
#                         max_charsum = ord(str[0]) + ord(str[-1])
#                         difference = distance
#                         result = str
#                     elif len(str) == max_length:
#                         charsum = ord(str[0]) + ord(str[-1])
#                         if charsum > max_charsum:
#                             max_charsum = charsum
#                             difference = distance
#                             result = str
#                         elif charsum == max_charsum:
#                             if distance < difference:
#                                 difference = distance
#                                 result = str
#             print(result)