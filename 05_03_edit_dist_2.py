# The minimum number of single-symbol insertions, deletions, and 
# substitutions to transform one string into the other one.
def edit_dis(A,B) :
    n, m = len(A), len(B)
    fkey = str(n) + str(m)
    Als = [0] + [*A] # Alst [0,1...n]
    Bls = [0] + [*B] # Blst [0,1...m]

    D = {}
    D['00'] = 0 # Dij, i for A, j for B

    for i in range(1,n+1) :
        key = str(i) + '0'
        D[key] = i
    for j in range(1,m+1) :
        key = '0' + str(j)
        D[key] = j
    
    for j in range(1,m+1) :
        for i in range(1,n+1):
            key = str(i) + str(j)
            inst = D[str(i) + str(j-1)] + 1
            delete = D[str(i-1) + str(j)] + 1
            match = D[str(i-1) + str(j-1)]
            mmatch = D[str(i-1) + str(j-1)] + 1
            if Als[i] == Bls[j] :
                D[key] = min(inst,delete,match)
            else :
                D[key] = min(inst,delete,mmatch)
#    print(D)
    return D[fkey]

if __name__ == '__main__':
    A = input()
    B = input()
    print(edit_dis(A,B))


