# Partition a set of integers into three subsets with equal sums.
def split_three(n,gls) :
    # find GCD of gls
    cls = []
    for i in range(n):
        cls.append(gls[i])
    for i in range(n-1) :
        x = GCD(cls[i],cls[i+1])
        cls[i+1] = x
    gcd = cls[-1]
    
    # each item in gls divide gcd
    for i in range(n) :
        new = gls[i] // gcd
        gls[i] = new
    
    # check if gls could be separte into 3 share
    rem = sum(gls) % 3
    if rem > 0 : return 0      
    
    # find if gls could fill the backpack
    W = sum(gls) // 3
    gls = [0] + gls
    W1 = max_goldv(W,n,gls)
#    print('3:',W,W1)
    if W != W1 :
        return 0
    W2 = max_goldv(W,n,gls)
#    print('4:',W,W2)
    if W == W2 :
        return 1
    else :
        return 0


def max_goldv(W,n,gls) :
#    print('1:',W,n,gls)
    A, B, chls = [], [], []
    for i in range(W+1):
        A.append([0,[-1]])
        B.append([0,[-1]])
    
    r = 1
    for i in range(1,n+1) :
        wi = gls[i]
        for w in range(W+1) :
#            print('2:',i,w,wi)
            if r % 2 == 1 :
                if w == 0 or wi > w:
                    B[w][0] = 0
                    continue
                else :
                    xuse = A[w][0]
                    use = A[w-wi][0] + wi
                    if xuse <= use :
                        B[w][0] = use
                        B[w][1] = A[w-wi][1] + [i]
#                        print('2-1:',w,B[w])
                    else : 
                        B[w][0] = xuse
                        B[w][1] = A[w][1]
#                        print('2-2:',w,B[w])
            else :
                if w == 0 or wi > w :
                    A[w][0] = 0
                    continue
                else :
                    xuse = B[w][0]
                    use = B[w-wi][0] + wi
                    if xuse <= use :
                        A[w][0] = use
                        A[w][1] = B[w-wi][1] + [i]
#                        print('2-3:',A[w])
                    else : 
                        A[w][0] = xuse
                        A[w][1] = B[w][1]
#                        print('2-4:',A[w])
        r += 1

    if r % 2 == 1 :
        ans = A[-1]
    else :
        ans = B[-1]
    
    for i in ans[1] :
        if i != -1 :
            gls[i] = 0
    
    return ans[0]

def GCD(num1,num2) :
    numa,numb = int(num1),int(num2)
    if numa == 0 or numa % numb == 0 : return numb
    if numb == 0 or numb % numa == 0 : return numa
    for i in range(min(numa,numb)+1) :
        rema = numa % numb
        if rema == 0 :
            return numb
        else:
            numa = numb
            numb = rema

if __name__ == '__main__' :
    n = int(input())
    gls = list(map(int,input().split()))
    print(split_three(n,gls))