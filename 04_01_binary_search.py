# Search a key in a sorted array of keys.
# Input n int in K array, m int in Q array
# Output find the corresponding i where K[i]=Q[0...m-1]
def bi_search(n,klst,m,qlst) :
    for i in range(m) :
        maxi, mini = n - 1, 0
        while True :
            midi = (maxi + mini) // 2
            k, q = klst[midi], qlst[i]
            if q == k :
                qlst[i] = midi
                break
            elif midi == mini and q == klst[maxi] :
                qlst[i] = maxi
                break
            elif midi == mini and q != klst[maxi] :
                qlst[i] = -1
                break
            elif qlst[i] < klst[midi] :
                maxi = midi - 1
                mini = mini
            else :
                maxi = maxi
                mini = midi + 1
    return qlst

if __name__ == '__main__':
    n = int(input())
    klst = list(map(int,input().split()))
    m = int(input())
    qlst = list(map(int,input().split()))
    ans = map(str,bi_search(n,klst,m,qlst))
    print(' '.join(ans))
