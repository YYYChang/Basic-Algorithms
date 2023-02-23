# Represent a positive integer as the sum of the
# maximum number of pairwise distinct positive integers.
def max_num_pair(num) :
    sum = 0
    intlst = []
    for i in range(1,num+1):
        if sum + i + (i+1) <= num :
            intlst.append(i)
            sum += i
        else :
            last = num - sum
            if last > 0 :
                intlst.append(num-sum)
            break
    return intlst

if __name__ == '__main__':
    num = int(input())
    ans = max_num_pair(num)
    ans2 = map(str,ans)
    print(len(ans))
    print(' '.join(ans2))
