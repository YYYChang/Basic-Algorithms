# Compute the maximum length of a common subsequence of three sequences.
def edit_dis_three(n,m,o,A,B,C) :
    Als = [0] + A # Alst [0,1...n]
    Bls = [0] + B # Blst [0,1...m]
    Cls = [0] + C # Clst [0,1...o]
    ABls = [0] + com_seq(n,m,Als,Bls)
    ABCls = com_seq(len(ABls)-1,o,ABls,Cls)
    return len(ABCls)

def com_seq(n,m,A,B) :
    fkey = str(n) + str(m)
    print('0:',n,m,A,B)
    D = {}
    D['00'] = [0,[-1]] # Dij, i for A, j for B

    for i in range(1,n+1) :
        key = str(i) + '0'
        D[key] = [i,[-1]]
    for j in range(1,m+1) :
        key = '0' + str(j)
        D[key] = [j,[-1]]
    
    for j in range(1,m+1) :
        for i in range(1,n+1):
            print('1:',i,j)
            key = str(i) + str(j)

            dio = D[str(i-1) + str(j-1)]
            de = D[str(i-1) + str(j)]
            it = D[str(i) + str(j-1)]

            inst = it[0] + 1
            delete = de[0] + 1
            match = dio[0]
            mmatch = dio[0] + 1
            print('2:','key',key,'inst',inst,'del',delete,'mat',match,'mm',mmatch)

            if A[i] == B[j] :
                if match <= inst and match <= delete :
                    D[key] = [match,dio[1]+[i]]
                    print('3-1-1:',D[key])
                elif delete < inst and delete < match :
                    D[key] = [delete,de[1]]
                    print('3-1-2:',D[key])
                else :
                    D[key] = [inst,it[1]]     
                    print('3-1-3:',D[key])
            else :
                if mmatch < inst and mmatch < delete :
                    D[key] = [mmatch,dio[1]]
                    print('3-2-1:',D[key])
                elif delete < inst and delete < mmatch :
                    D[key] = [delete,de[1]]
                    print('3-2-2:',D[key])
                elif inst < delete and inst < mmatch :
                    D[key] = [inst,it[1]]
                    print('3-2-3:',D[key])
                elif mmatch == inst and mmatch < delete :
                    if len(dio[1]) >= len(it[1]) :
                        D[key] = [mmatch,dio[1]]
                    else :
                        D[key] = [inst,it[1]]         
                    print('3-2-4:',D[key])           
                elif mmatch == delete and mmatch < inst :
                    if len(dio[1]) >= len(de[1]) :
                        D[key] = [mmatch,dio[1]]
                    else :
                        D[key] = [delete,de[1]]  
                    print('3-2-5:',D[key])                  
                elif inst == delete and inst < mmatch :
                    if len(it[1]) >= len(de[1]) :
                        D[key] = [inst,it[1]]
                    else :
                        D[key] = [delete,de[1]] 
                    print('3-2-6:',D[key])     
                else :
                    if len(dio[1]) >= len(it[1]) and len(dio[1]) >= len(de[1]) :
                        D[key] = [mmatch,dio[1]]
                    elif len(dio[1]) < len(it[1]) and len(it[1]) >= len(de[1]) :
                        D[key] = [inst,it[1]]   
                    else :
                        D[key] = [delete,de[1]]  

    comls = []
    ans = D[fkey]
    for i in range(len(ans[1])) :
        print('4:',ans,ans[1][i])
        if ans[1][i] != -1 :
            comls.append(A[i])
    print('5:',comls)
    return comls

if __name__ == '__main__':
    n = int(input())
    A = input().split()
    m = int(input())
    B = input().split()
    o = int(input())
    C = input().split()
    print(edit_dis_three(n,m,o,A,B,C))


