def solve(n,start_x,start_y,src_x,src_y,trg_x,trg_y):
    while n>1:
        half_len=2**(n-1)
        half_x=start_x+half_len
        half_y=start_y+half_len
        src=0
        if src_x<half_x:
            if src_y<half_y:
                src=1
            else:
                src=2
        else:
            if src_y<half_y:
                src=3
            else:
                src=4
        if trg_x<half_x:
            if trg_y<half_y:
                if src==1:
                    pass
                else:
                    src_x=half_x-1
                    src_y=half_y-1
                    if src_x == trg_x and src_y == trg_y:
                        if src==2:
                            print(src_x+1,' ',src_y,',',src_x+1,' ',src_y+1,sep='')
                        elif src==3:
                            print(src_x,' ',src_y+1,',',src_x+1,' ',src_y+1,sep='')
                        else:
                            print(src_x,' ',src_y+1,',',src_x+1,' ',src_y,sep='')
                        return
            else:
                start_y=half_y
                if src==2:
                    pass
                else:
                    src_x=half_x-1
                    src_y=half_y
                    if src_x == trg_x and src_y == trg_y:
                        if src==1:
                            print(src_x+1,' ',src_y-1,',',src_x+1,' ',src_y,sep='')
                        elif src==3:
                            print(src_x,' ',src_y-1,',',src_x+1,' ',src_y,sep='')
                        else:
                            print(src_x,' ',src_y-1,',',src_x+1,' ',src_y-1,sep='')
                        return
        else:
            start_x=half_x
            if trg_y<half_y:
                if src==3:
                    pass
                else:
                    src_x=half_x
                    src_y=half_y-1
                    if src_x == trg_x and src_y == trg_y:
                        if src==1:
                            print(src_x-1,' ',src_y+1,',',src_x,' ',src_y+1,sep='')
                        elif src==2:
                            print(src_x-1,' ',src_y,',',src_x,' ',src_y+1,sep='')
                        else:
                            print(src_x-1,' ',src_y,',',src_x-1,' ',src_y+1,sep='')
                        return
            else:
                start_y=half_y
                if src==4:
                    pass
                else:
                    src_x=half_x
                    src_y=half_y
                    if src_x == trg_x and src_y == trg_y:
                        if src==1:
                            print(src_x-1,' ',src_y,',',src_x,' ',src_y-1,sep='')
                        elif src==2:
                            print(src_x-1,' ',src_y-1,',',src_x,' ',src_y-1,sep='')
                        else:
                            print(src_x-1,' ',src_y-1,',',src_x-1,' ',src_y,sep='')
                        return
        n-=1
    pair = []
    for x in range(start_x,start_x+2):
        for y in range(start_y,start_y+2):
            if not ((x == src_x and y == src_y) or (x == trg_x and y == trg_y)):
                pair.append(str(x)+' '+str(y))
    print(','.join(pair))

if __name__ == '__main__':
    test_cnt=int(input())
    for t in range(test_cnt):
        n,src_x,src_y=[int(x) for x in input().split()]
        trg_x,trg_y=[int(x) for x in input().split()]
        solve(n,0,0,src_x,src_y,trg_x,trg_y)