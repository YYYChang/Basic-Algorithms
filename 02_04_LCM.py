#LCM
def GCD(num1,num2) :
    numa,numb = int(num1),int(num2)
    if numa == 0 or numa % numb == 0 : return numb
    if numb == 0 or numb % numa == 0 : return numa
    for i in range(1, numa*numb+1) :
        rema = numa % numb
        if rema == 0 :
            return numb
        else:
            numa = numb
            numb = rema

if __name__ == '__main__':
    numbers = input().split()
    a, b = map(int,numbers)
    LCM = int(a * b / GCD(a,b))
    print(LCM)
