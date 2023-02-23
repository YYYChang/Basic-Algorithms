#sum all Fibonacci Number <= n
def sum_fibo(a) :
    n = a % 30

    if n <= 1 :
        return n

    Fn_1, Fn_2, Sum = 1, 0, 1

    for i in range(n-1) :
        Fn_1, Fn_2 = (Fn_1 + Fn_2) % 10, Fn_1 % 10
        Sum = (Sum + Fn_1 * Fn_1) % 10

    return Sum % 10

if __name__ == '__main__':
    print(sum_fibo(int(input())))
