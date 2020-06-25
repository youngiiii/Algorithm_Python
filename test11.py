def num(k,n):
    if n == 1:
        return 1
    elif k == 0:
        return n
    else:
        return num(k-1, n) + num(k, n-1)

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    print(num(k,n))