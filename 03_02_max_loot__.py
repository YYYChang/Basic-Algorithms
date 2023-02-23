# Find the maximal value of items that fit into the backpack.
def max_val(kinds,capacity) :
    if capacity == 0 : return 0

    upl, wl = [], []
    for i in range(kinds) :
        price, weights = map(int,input().split())
        upl.append(price/weights)
        wl.append(weights)

    for i in range(kinds) :
        for j in range(kinds-1) :
            if upl[j] < upl[j+1] :
                k = upl[j]
                upl[j] = upl[j+1]
                upl[j+1] = k

                k = wl[j]
                wl[j] = wl[j+1]
                wl[j+1] = k
    total = 0
    for i in range(kinds) :
        up, w = upl[i], wl[i]
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
