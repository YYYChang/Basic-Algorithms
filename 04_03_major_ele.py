# Check whether a given sequence of numbers contains
# an element that appears more than half of the times.
def major_ele(n,mlst) :
    mdic = dict()
    count = 0
    for m in mlst :
        mdic[m] = mdic.get(m,0) + 1
    for k, v in mdic.items() :
        if v > n/2 :
            return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    mlst = list(map(int,input().split()))
    print(major_ele(n,mlst))
