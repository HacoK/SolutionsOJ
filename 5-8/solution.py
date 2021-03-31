def find_longest(threshod,left,right):
    dp_left = []
    list_left = []
    for i in range(len(left)):
        if left[i] > threshod:
            continue
        j = len(dp_left)-1
        while j>=0 and min(dp_left[j])>=left[i]:
            j -= 1
        if j==-1:
            if len(dp_left)!=0:
                dp_left[0].append(left[i])
                list_left[0].append([left[i]])
            else:
                dp_left.append([left[i]])
                list_left.append([[left[i]]])
        elif j==len(dp_left)-1:
            dp_left.append([left[i]])
            prev = list_left[j]
            current = []
            for item in prev:
                if max(item) < left[i]:
                    current.append(item+[left[i]])
            list_left.append(current)
        else:
            dp_left[j+1].append(left[i])
            prev = list_left[j]
            current = []
            for item in prev:
                if max(item) < left[i]:
                    current.append(item+[left[i]])
            list_left[j+1] += current

    dp_right = []
    list_right = []
    for i in range(len(right)):
        if right[i] > threshod:
            continue
        j = len(dp_right)-1
        while j>=0 and min(dp_right[j])>=right[i]:
            j -= 1
        if j==-1:
            if len(dp_right)!=0:
                dp_right[0].append(right[i])
                list_right[0].append([right[i]])
            else:
                dp_right.append([right[i]])
                list_right.append([[right[i]]])
        elif j==len(dp_right)-1:
            dp_right.append([right[i]])
            prev = list_right[j]
            current = []
            for item in prev:
                if max(item) < right[i]:
                    current.append(item+[right[i]])
            list_right.append(current)
        else:
            dp_right[j+1].append(right[i])
            prev = list_right[j].copy()
            current = []
            for item in prev:
                if max(item) < right[i]:
                    current.append(item+[right[i]])
            list_right[j+1] += current

    global length,result
    cur_length = len(dp_left)+len(dp_right)+1

    if(len(list_left)==0):
        left = [str(threshod)]
    else:
        left = []
        for item in list_left[-1]:
            left.append(' '.join(map(str,item))+' '+str(threshod))
    if(len(list_right)==0):
        right = ['']
    else:
        right = []
        for item in list_right[-1]:
            right.append(' '+' '.join(map(str,reversed(item))))

    if cur_length > length:
        length = cur_length
        result = []
        for l in left:
            for r in right:
                result.append(l+r)
    elif cur_length == length:
        for l in left:
            for r in right:
                result.append(l+r)

if __name__ == "__main__":
    for _ in range(int(input())):
        arr = [int(x) for x in input().split()]
        length = 0
        result = []
        for i in range(len(arr)):
            find_longest(arr[i],arr[0:i],list(reversed(arr[i+1:])))
        for result in sorted(result):
            print(result)