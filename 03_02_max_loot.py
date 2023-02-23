# Find the maximal value of items that fit into the backpack.
def max_val(kinds,capacity) :
    if capacity == 0 : return 0

    mtrl = list()
    for i in range(kinds) :
        price, weights = map(int,input().split())
        mtrl.append((price/weights, weights))

    mtrls = sorted(mtrl,reverse=True)
    total = 0
    for j in range(kinds) :
        up, w = mtrls[j]
        if w <= capacity :
            total += up * w
            capacity -= w
        else :
            total += up * capacity
            capacity = 0

        if capacity == 0 : break

    return total

if __name__ == '__main__':
    kinds, capacity = map(int,input().split())
    print('%.4f' % max_val(kinds,capacity))
