# Find the minimum number of points needed to cover all given segments on a line.
def collect_seg(num,stlst,endlst) :
    tlst, seg = [], 0
    while len(stlst) > 0:
        stmin, endmax = min(stlst), max(endlst)
        maxt = 0
        for x in range(stmin,endmax+1) :
            touch, segt = 0, []
            for i in range(len(stlst)) :
                if stlst[i] <= x and x <= endlst[i] :
                    touch += 1
                    segt.append(i)
            if touch > maxt :
                xcord = x
                maxt = touch
                seglst = segt
        tlst.append(xcord)
        count = 0
        for i in seglst :
            stlst.pop(i-count)
            endlst.pop(i-count)
            count += 1
    return tlst

if __name__ == '__main__':
    num = int(input())
    if num == 0 :
        print(0)
    else :
        stlst, endlst = [], []
        for i in range(num) :
            start, end = map(int,input().split())
            stlst.append(start)
            endlst.append(end)
    ans = collect_seg(num,stlst,endlst)
    ans2 = map(str,sorted(ans))
    print(len(ans))
    print(' '.join(ans2))
