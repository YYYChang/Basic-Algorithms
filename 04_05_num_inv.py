# Compute the number of inversions in a sequence of integers.
def num_inv(num,numls) :
    if num > 1:

        mid = num//2 
        par1 =numls[:mid] + [numls[num]]
        par2 = numls[mid:num] + [numls[num]]
#        print('1:',num,numls,mid,par1)
#        print('2:',num,numls,mid,par2)
        num_inv(len(par1)-1,par1)
        num_inv(len(par2)-1,par2)

        st = s1n = s2n = invt = s2f = 0
#        print('3:',par1,par2)
        while s1n < len(par1)-1 and s2n < len(par2)-1 :
            if par1[s1n] <= par2[s2n] :
                numls[st] = par1[s1n]
                s1n += 1
                invt += s2f
            else:
                numls[st] = par2[s2n]
                s2n += 1
                s2f += 1
            st += 1
#            print(st,s1n,s2n)

        while s1n < len(par1)-1 :
                numls[st] = par1[s1n]
                s1n += 1
                st += 1
                invt += s2f

        while s2n < len(par2)-1 :
                numls[st] = par2[s2n]
                s2n += 1
                st += 1

        numls[num] = par1[-1] + par2[-1] + invt    
        
#        print('4:',numls)


if __name__ == '__main__':
    num = int(input())
    numls = list(map(int,input().split())) + [0]
    num_inv(num,numls)
#    print(numls[:-1])
    print(numls[-1])