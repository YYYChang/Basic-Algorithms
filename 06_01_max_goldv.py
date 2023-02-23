# Given a set of gold bars of various weights and a backpack that can hold
# at most W pounds, place as much gold as possible into the backpack.
def max_goldv(W,n,gls) :
    cls = gls
    gls = [0] + gls
    for i in range(n-1) :
        x = GCD(cls[i],cls[i+1])
        cls[i+1] = x
    gcd = cls[-1]
    for i in range(n) :
        gls[i] = gls[i] // gcd
    
    A, B = [], []
    for i in range(W+1):
        A.append(0)
        B.append(0)
    
    r = 1
    for i in range(1,n+1) :
        wi = gls[i]
        for w in range(W+1) :
            if r % 2 == 1 :
                if w == 0 :
                    B[w] = 0
                    continue
                else :
                    maxv = A[w]
                    if wi <= w :
                        val = A[w-wi] + wi
                        if val > maxv :
                            maxv = val
                    B[w] = maxv
            else :
                if w == 0 :
                    A[w] = 0
                    continue
                else :
                    maxv = B[w]
                    if wi <= w :
                        val = B[w-wi] + wi
                        if val > maxv :
                            maxv = val
                    A[w] = maxv
        r += 1
    if r % 2 == 1 :
        return A[-1]*gcd
    else :
        return B[-1]*gcd

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

if __name__ == '__main__':
    W, n = map(int,input().split())
    gls = list(map(int,input().split()))
    print(max_goldv(W,n,gls))