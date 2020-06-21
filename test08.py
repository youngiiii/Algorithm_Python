# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 
# 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# def Calc(num, lst):
#     tmp = 1
#     for v in range(1, num * 2):
#         if num > v:
#             lst.append(tmp)
#             tmp += 1
#         elif num == v:
#             lst.append(tmp)
#             tmp -= 1
#         elif num < v:
#             lst.append(tmp)
#             tmp -= 1


# num = int(input())

# up = list()
# dn = list()

# for v in range(1, num):
#     if v % 2 == 1:
#         Calc(v, up)
#     else :
#         Calc(v, dn)

# print(up[num - 1], end='')
# print("/", end='')
# print(dn[num - 1], end='')

X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')