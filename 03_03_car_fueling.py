# Compute the minimum number of gas tank refills to get from one city to another.
def car_fuel(d,m,n,stplst) :
    stop, nxstpl = 0, m
    for i in range(n) :
        # except last stop
        if i < n-1 :
            if nxstpl >= stplst[i] and nxstpl < stplst[i+1] :
                stop += 1
                nxstpl = m + stplst[i]
            if nxstpl >= d : break
        # last stop
        elif nxstpl >= stplst[i] :
            stop += 1
            nxstpl = m + stplst[i]

    if nxstpl >= d :
        return stop
    else :
        return -1

if __name__ == '__main__':
    d, m, n = map(int,(input(),input(),input()))
    if d <= m :
        print(0)
    elif d > m and n == 0 :
        print(-1)
    else :
        stplst = list(map(int,input().split()))
        print(car_fuel(d,m,n,stplst))
