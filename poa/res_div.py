def makebinary(a):
    return '0'+bin(a)[2:]


def add(a,b):
    sum = int(a,2)+int(b,2)
    sum = makebinary(sum)
    return sum


def twoscomp(a):
    a_len = len(a)
    a = a.replace('0','2')
    a = a.replace('1','0')
    a = a.replace('2','1')
    a = add(a,'0'*(len(a)-1)+'1')
    if len(a)>a_len:
        a = a[(len(a)-a_len):]
    else:
        a = abs(len(a)-a_len)*'0' + a
    return a


def ShiftLeft(A,Q):
    A = list(A)
    Q = list(Q)
    Acp = A.copy()
    Qcp = Q.copy()
    for i in range(len(A)-1):
        A[i] = Acp[i+1]
    A[len(A)-1] = Q[0]
    for i in range(len(Q)-1):
        Q[i] = Qcp[i+1]
    A = ''.join(A)
    Q = ''.join(Q)
    return A,Q


def res_div(Q,M,A,M1,n):
    print(A+' '+Q)
    while(n>0):
        A,Q = ShiftLeft(A,Q)
        sum = add(A,M1)
        A = sum[(len(sum)-len(Q)):]
        if A[0] == '1':
            Q = list(Q)
            Q[len(Q)-1] = '0'
            Q = ''.join(Q)
            sum = add(A,M)
            A = sum[(len(sum)-len(Q)):]
            A = abs(len(A)-len(Q))*'0'+A
        else:
            Q = list(Q)
            Q[len(Q)-1] = '1'
            Q = ''.join(Q)
        n -= 1
        print(A+' '+Q)
    return A,Q


if __name__ == '__main__' :
    Q = input("Enter Q : ")
    M = input("Enter M : ")
    neg = 0
    Q,M = int(Q), int(M)
    if Q<0:
            Q = Q*-1
            neg += 1
    if M<0:
           M = M*-1
           neg += 1
    Q = makebinary(Q)
    M = makebinary(M)
    filler = ''+abs(len(M)-len(Q))*'0'
    if len(M)<len(Q):
        M = M[0]+filler+M[1:]
    else :
        Q = Q[0]+filler+Q[1:]
    A = '0'*len(Q)
    M1 = twoscomp(M)
    rem,quo = res_div(Q,M,A,M1,len(Q))
    print(f"Quotient is {quo}( i.e. {int(quo,2)}) and Remainder is {rem}( i.e. {int(rem,2)})")