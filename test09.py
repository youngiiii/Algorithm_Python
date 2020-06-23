A, B, V = map(int, input().split())

day=1
while V>0:
    V-=A
    if V<=0:
        break
    V+=B
    day+=1

print(day)