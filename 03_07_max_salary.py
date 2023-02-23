# Compile the largest number by concatenating the given numbers.
def max_salary(num, strl) :
    seq, intchk = [], []
    while len(intchk) < num :
        maxs = 0
        for i in range(num) :
            if i not in intchk :
                a = int(strl[i][0])
                if a > maxs :
                    maxs = a
                    maxi = i
                elif a == maxs and (strl[i]+strl[maxi] > strl[maxi]+strl[i]) == True :
                    maxi = i
        intchk.append(maxi)
        seq.append(strl[maxi])
    return ''.join(seq)

if __name__ == '__main__':
    num = int(input())
    strl = input().split()
    print(max_salary(num, strl))
