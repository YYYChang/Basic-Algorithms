# Find the minimum number of operations needed to get a positive integer n from 
# 1 by using only three operations: add 1, multiply by 2, and multiply by 3. 
def prim_cal(num) :
    # cal type +1, *2, and *3
    if num == 1 :
        return 0
    cir = 2 * num // 3 + 1
    mincls = [(0,[])] # min calculate list
    for i in range(1,cir) :
        mincls.append(0)
    
    for n in range(1,num) :
        mincal = None
        pos = n % cir 
#        print('1:','n',n,'pos',pos,'cir',cir,mincls)
        if (n + 1) % 3 == 0 :
            spos = ((n + 1) // 3 % cir) -1
            if spos < 0 :
                spos = cir - 1
#            print('2-1-1:','mincal',mincal,'spos',spos)
            if mincal == None or mincal > mincls[spos][0] + 1 :
                mincal = mincls[spos][0] + 1
                itern = mincls[spos][1] + ['*3']
#            print('2-1-2:','mincal',mincal,'spos',spos)
        if (n + 1) % 2 == 0 :
            spos = ((n + 1) // 2 % cir) -1
            if spos < 0 :
                spos = cir - 1
#            print('2-2-1:','mincal',mincal,'spos',spos)
            if mincal == None or mincal > mincls[spos][0] + 1 :
                mincal = mincls[spos][0] + 1
                itern = mincls[spos][1] + ['*2']
#            print('2-2-2:','mincal',mincal,'spos',spos)
        spos = n % cir - 1
        if spos < 0 :
            spos = cir - 1
#        print('2-3-1:','mincal',mincal,'spos',spos)
        if mincal == None or mincal > mincls[spos][0] + 1 :
            mincal = mincls[spos][0] + 1
            itern = mincls[spos][1] + ['+1']
#        print('2-3-2:','mincal',mincal,'spos',spos)
        mincls[pos] = (mincal,itern)
#        print('2-4:',mincls)

#    print('3:', mincls)
    return mincls[pos]

if __name__ == '__main__':
    num = int(input())
    if num == 1 :
        print('0')
        print('1')
    else :
        ans = prim_cal(num)
#        print(ans)
        time = ans[0]
        calls = ans[1]
        calnum = len(calls)
        iternls = [] # internal num list
        for i in range(calnum) :
            iternls.append(0)
        iternls.append(str(num))
        for i in range(calnum) :
            j = calnum - 1 - i
            if calls[j] == '*3' :
                num = num // 3
                iternls[j] = str(num)
            elif calls[j] == '*2' :
                num = num // 2
                iternls[j] = str(num)
            else:
                num = num - 1
                iternls[j] = str(num)
        print(time)
        print(' '.join(iternls))


