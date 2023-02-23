# Compute the min num of coins needed to change the
# input into coins with denominations 1, 5, and 10.
def money_change(money) :
    coins = 0
    if money > 0 :
        coins = money // 10 + money % 10 //5 + money % 5
    return coins

if __name__ == '__main__':
    money = int(input())
    print(money_change(money))
