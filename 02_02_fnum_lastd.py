#print the last digit of Fibonacci Number
def Caculate(a) :
    if a <= 1 : return a

    n = a % 60
    if n == 0 : n = 60

    Fn_1, Fn_2 = 1, 0

    for i in range(n-1) :
        Fn_1, Fn_2 = (Fn_1 + Fn_2) % 10, Fn_1 % 10

    return Fn_1 % 10

if __name__ == '__main__':
    Fnum = Caculate(int(input()))
    print(Fnum)
