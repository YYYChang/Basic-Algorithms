# The minimum number of single-symbol insertions, deletions, and 
# substitutions to transform one string into the other one.
def edit_dis(A,B) :
    n, m = len(A), len(B)
    Als = [0] + [*A] # Alst [0,1...n]
    Bls = [0] + [*B] # Blst [0,1...m]

    D = []
    for i in range(n+1) :
        D.append(0)
    
    for j in range(m+1) :
        for i in range(n+1):
#            print('1:',i,j,D)
            if j == 0 :
                D[i] = i
                continue
            elif i == 0 :
                delete = j + 1
                continue
            inst = D[i] + 1
            match = D[i-1]
            mmatch = D[i-1] + 1
#            print('2:','delete',delete,'inst',inst,'ma',match,'mma',mmatch)
            if Als[i] == Bls[j] :
                cur = min(inst,delete,match)
            else :
                cur = min(inst,delete,mmatch)
            D[i-1] = delete - 1
            delete = cur + 1
            if i == n :
                D[i] = cur
#            print('3:',i,j,D)
    return D[n]

if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    print(edit_dis(A,B))


