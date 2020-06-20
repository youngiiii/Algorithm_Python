def Calc(num, lst):
    tmp = 1
    for v in range(1, num * 2):
        if num > v:
            lst.append(tmp)
            tmp += 1
        elif num == v:
            lst.append(tmp)
            tmp -= 1
        elif num < v:
            lst.append(tmp)
            tmp -= 1


num = int(input())

up = list()
dn = list()

for v in range(1, num):
    if v % 2 == 1:
        Calc(v, up)
    else :
        Calc(v, dn)

print(up[num - 1], end='' )
print("/", end='')
print(dn[num - 1], end='')


