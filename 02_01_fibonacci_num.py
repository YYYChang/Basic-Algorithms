#Fibonacci Number - need to remember list
def Caculate(n) :
    Flist = list()
    for i in range(n+1) :
        if i <= 1 :
            Flist.append(i)
        else :
            Flist.append( Flist[i-1] + Flist[i-2] )
    return Flist[n]
#Fibonacci Number
def Caculate2(n) :
    if n <= 1 :
        return n
    Fn_1 = 1
    Fn_2 = 0
    for i in range(n-2) :
        Fn_1, Fn_2 = Fn_1 + Fn_2, Fn_1
    return(Fn_1 + Fn_2)

if __name__ == '__main__':
    Fnum = Caculate2(int(input()))
    print(Fnum)
#    print(str(Fnum)[-1])
