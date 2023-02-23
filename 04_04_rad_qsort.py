# Sort a given sequence of numbers (that may contain duplicates) using a modification
# of RandomizedQuickSort that works in O(nlogn) expected time.
def swap(lst,i,j) :
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp    

def rad_sort(num,nls) :
    if num > 1:
        import random
        ploc = random.randint(0,num-1)

#        print('1:',ploc,nls[ploc],nls)

        swap(nls,0,ploc)
        ploc = j = k = 0
        for i in range(1,num) :
#            print('1-1',i,'np:',nls[ploc],'ni',nls[i],j,k,nls)
            if nls[i] < nls[ploc] : 
                swap(nls,j+1,i)
                if k != j :
                    swap(nls,k+1,i)
                j += 1
                k += 1
#                print('1-2',nls[ploc],i,j,k,nls)
            elif nls[i] == nls[ploc] :
                swap(nls,k+1,i)
                k += 1
#                print('1-3',nls[ploc],i,j,k,nls)
        swap(nls,ploc,j) #ploc = j~k
        sn = nls[:j]
        bn = nls[k+1:]
    
#        print('2:',sn,bn,nls)
    
        rad_sort(len(sn),sn)
        rad_sort(len(bn),bn)

#        print('3:',sn,bn)

        for i in range(num) :
            if j <= i <= k : continue
            elif i < j :
                nls[i] = sn[i]
            else :
                nls[i] = bn[i-(k+1)]
        
#        print('4:',nls)

        
if __name__ == '__main__':
    num = int(input())
    nls = list(map(int,input().split()))
    rad_sort(num,nls)
    ans = map(str,nls)
    print(' '.join(ans))
