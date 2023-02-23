#sum all Fibonacci Number <= n
def par_sum_fibo(n, m) :
    a, b = n % 60, m % 60
    if n == 0 : a = 0
    elif a == 0 : a = 60
    elif b == 0 : b = 60

    current, next, sum1, sum2 = 0, 1, 0, 0

    for i in range(max(a,b)+1) :
        if a != 0 and i <= a-1 :
            sum1 = (sum1 + current) % 10
        if i <= b :
            sum2 = (sum2 + current) % 10
        next, current = (current + next) % 10, next % 10
    return (sum2 + 10 - sum1) % 10

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(par_sum_fibo(n,m))
