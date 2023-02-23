#deal with huge Fibonacci Number
def huge_naive(n, m) :
    if n <= 1 : return n

    Flist = [0,1]
    Fn1, Fn2 = 1, 0

    for i in range(n-1) :
        Fn1, Fn2 = (Fn1 + Fn2) % m, Fn1 % m
        Flist.append(Fn1 % m)
        half = (len(Flist) - 1) // 2
        if i > 1 and Flist[1:half+1] == Flist[half+1:] :
            index = n % half
            if index == 0 : index = half
            break
        index = i + 2
    return Flist[index]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(huge_naive(n,m))
