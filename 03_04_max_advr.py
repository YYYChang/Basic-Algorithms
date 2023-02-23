# Find the maximum dot product of two sequences of numbers.
def max_dot(num,prices,clicks) :
    prices.sort(reverse = True)
    clicks.sort(reverse = True)

    dotp = 0
    for i in range(num) :
        dotp += prices[i] * clicks[i]
    return dotp

if __name__ == '__main__':
    num = int(input())
    if num == 0 :
        print(0)
    else :
        prices = list(map(int,input().split()))
        clicks = list(map(int,input().split()))
        print(max_dot(num,prices,clicks))
