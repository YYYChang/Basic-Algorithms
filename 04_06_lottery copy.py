# Given a set of points and a set of segments on a line,
# compute, for each point, the number of segments it is contained in.
def lottery(n,m,llst,rlst,xlst) :
    # create index && ans list
    ilst, ans = [], []
    for i in range(m) :
        ilst.append(i)
        ans.append(0)

    syn_rsort(n,m,llst,rlst,xlst,ilst)

    for i in range(m) :
        ans[ilst[i]] = xlst[i]

    print('XLST:',xlst,ilst)
    
    return ans 

def syn_rsort(n,m,llst,rlst,xlst,ilst) :
    if m > 0 :
        import random
        p = random.randint(0,m-1)
        key = xlst[p]
        
        print('1:','Key',key,'llst,rlst',llst,rlst,'xlst',xlst)
        
        # rad sort line list
        # p1: the next place to change < ; p2: the next place to change =       
        p1, p2 = 0, 0 
        for i in range(n) :
            if rlst[i] < key :
                syn_swap(rlst,llst,i,p1)
                if p2 != p1 :
                    syn_swap(rlst,llst,i,p2) 
                p1 += 1
                p2 += 1
            elif llst[i] <= key :
                syn_swap(rlst,llst,i,p2)              
                p2 += 1 
        
        # rad sort xlst
        m1, m2 = 0, 0   
        for i in range(m) :
            if xlst[i] < key :
                syn_swap(xlst,ilst,i,m1) 
                if m2 != m1 :
                    syn_swap(xlst,ilst,i,m2)          
                m1 += 1
                m2 += 1
            elif xlst[i] == key :
                syn_swap(xlst,ilst,i,m2)   
                m2 += 1 
        print('2:','key',key,'p1/p2/llst/rlst',p1,p2,llst,rlst,)
        print('2"','m1/m2/xlst',m1,m2,xlst)

        sllst, srlst, sxlst, silst = llst[:p2], rlst[:p2], xlst[:m1], ilst[:m1]
        bllst, brlst, bxlst, bilst = llst[p1:], rlst[p1:], xlst[m2:], ilst[m2:]
        print('S','key',key,'sllst,srlst',sllst,srlst,'sxlst,silst,xlst',sxlst,silst,xlst)
        print('B','key',key,'bllst,brlst',bllst,brlst,'bxlst,bilst,xlst',bxlst,bilst,xlst)
        if len(srlst) > 0 :
            syn_rsort(len(sllst),len(sxlst),sllst,srlst,sxlst,silst)  

        if len(bllst) > 0 :
            syn_rsort(len(bllst),len(bxlst),bllst,brlst,bxlst,bilst)

        #count touch
        for i in range(m):
            count = 0
            print('3-1:','p1/p2',p1,p2,'llst,rlst',llst,rlst,'sxlst,bxlst,xlst',sxlst,bxlst,xlst)
            print('3-1:','m1/m2',m1,m2,'i,xlst[i]',i,xlst[i],count)
            if m1 <= i < m2 :           
                for j in range(p2-p1) :
                    if llst[j+p1] <= xlst[i] <= rlst[j+p1] :
                        count += 1
                print('X',xlst[i],count)    
                xlst[i] = count
            elif i < m1 :
                print('Y',xlst[i],sxlst[i])
                xlst[i] = sxlst[i]
            else :
                print('Z',xlst[i],bxlst[i-m2])
                xlst[i] = bxlst[i-m2]

        if len(srlst) == 0 and len(sxlst) != 0 :
            for i in range(len(sxlst)) :
                print('3-2:',xlst[i],ilst[i],xlst)
                xlst[i] = 0

        elif len(brlst) == 0 and len(bxlst) != 0 :
            for i in range(len(bxlst)) :
                print('3-3:',xlst[i],ilst[i],xlst)           
                xlst[i+m2] = 0

        print('4:',xlst,ilst)

def swap(lst,i,j) :
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp    

def syn_swap(lst1,lst2,i,j) :
    temp = lst1[j]
    lst1[j] = lst1[i]
    lst1[i] =temp

    temp = lst2[j]
    lst2[j] = lst2[i]
    lst2[i] =temp
                
if __name__ == '__main__':
    n, m = map(int, input().split())
    llst, rlst = [], []
    for i in range(n) :
        l, r = map(int, input().split())
        llst.append(l)
        rlst.append(r)
    xlst = list(map(int, input().split()))
    ans = map(str,lottery(n,m,llst,rlst,xlst))
    print(' '.join(ans))
