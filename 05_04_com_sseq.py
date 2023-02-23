# Compute the maximum length of a common subsequence of two sequences.
def com_sseq(n,m,A,B) :
    Als = [0] + A # Alst [0,1...n]
    Bls = [0] + B # Blst [0,1...m]

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
#            print('2:','delete',delete,'inst',inst,'ma',match,'mma',mmatch)
            if Als[i] == Bls[j] :
                cur = min(inst,delete,match)
            else :
                cur = min(inst,delete)
            D[i-1] = delete - 1
            delete = cur + 1
            if i == n :
                D[i] = cur
#            print('3:',i,j,D)
    return int((n + m - D[n]) / 2)

if __name__ == '__main__':
    n = int(input())
    A = input().split()
    m = int(input())
    B = input().split()
    print(com_sseq(n,m,A,B))


