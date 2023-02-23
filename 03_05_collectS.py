# Find the minimum number of points needed to cover all given segments on a line.
def collect_seg(num,stlst,endlst) :
    xlst, tchk = [], []
    while len(tchk) < num:
        stmin, endmax = None, None
        for i in range(num) :
            if i not in tchk and (stmin == None or stlst[i] < stmin) :
                stmin = stlst[i]
            if i not in tchk and (endmax == None or endlst[i] > endmax) :
                    endmax = endlst[i]
        maxt = 0
        for x in range(stmin,endmax+1) :
            touch, tind = 0, []
            for i in range(num) :
                if i not in tchk :
                    if stlst[i] <= x <= endlst[i] :
                        touch += 1
                        tind.append(i)
            if touch > maxt :
                xcord = x
                maxt = touch
                tlst = tind
        xlst.append(xcord)
        for i in tlst :
            tchk.append(i)
    return xlst

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
