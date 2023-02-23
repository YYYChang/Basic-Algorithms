# Compute the minimum number of coins needed to change the 
# given value into coins with denominations 1, 3, and 4.
def money_ch(money) :
    coin = [1,3,4] # coin type 1, 3, and 4
    maxc = max(coin)
    cir = maxc + 1 
    mincls = [] # min change list
    for i in range(cir) :
        mincls.append(0)
    
    for m in range(money) :
        mincoin = None
        pos = m % cir
#        print('1:',m,pos,cir,mincls)
        for ctp in coin :
#            print('2:',ctp)
            if (m + 1) < ctp :
                continue
            elif (m + 1) > ctp :                
                spos = (m - ctp) % cir
                coinqt = mincls[spos] + 1
                if mincoin == None or coinqt < mincoin :
                    mincoin = coinqt
#                print('3-1:',spos,coinqt,mincoin)
            else :
                mincoin = 1
#                print('3-2:',mincoin)
                break      
        mincls[pos] = mincoin
#        print('4:',mincls)
     
    return mincls[pos]

if __name__ == '__main__':
    money = int(input())
    print(money_ch(money))

