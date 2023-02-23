def max_ae(ae) :
    import re 

    nls = list(map(int,re.findall('[0-9]+',ae)))
    ols = re.findall('[\+\-\*/]',ae)
    opdic = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
          '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    n= len(nls)

    ls = {}
    for i in range(n) :
        si = str(i)
        ls['m'+si+si] = nls[i]
        ls['M'+si+si] = nls[i]
    for s in range(1,n) :
        for i in range(n-s) :
            j = i + s
            si, sj = str(i), str(j)
            m, M = None, None
            for k in range(i,j) :
#                print('1:',i,k,k+1,j)
                op, sk, sk1 = ols[k], str(k), str(k+1)
                M1, m1, M2, m2 = ls['M'+si+sk], ls['m'+si+sk], ls['M'+sk1+sj], ls['m'+sk1+sj]
                print('2:',M1,m1,M2,m2)
                a = opdic[op](M1,M2)
                b = opdic[op](M1,m2)
                c = opdic[op](m1,M2)
                d = opdic[op](m1,m2)
#                print('2:',M1,m1,M2,m2,min(a,b,c,d),max(a,b,c,d))
                if m == None or m > min(a,b,c,d) :
                    m = min(a,b,c,d)
                if M == None or M < max(a,b,c,d) :
                    M = max(a,b,c,d)
            ls['m'+si+sj] = m
            ls['M'+si+sj] = M
#            print('3:',ls['M'+si+sj],ls['m'+si+sj])
    
    return ls['M'+si+sj]

if __name__ == '__main__' :
    ae = input()
    print(max_ae(ae))