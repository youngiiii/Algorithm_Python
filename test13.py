# X = int(input())
# count = 0
# result = [X]
# def calculation(x):
#     lst = []
#     for i in x:
#         lst.append(i-1)
#         if i%3 ==0:
#             lst.append(i/3)
#         if i%2 ==0:
#             lst.append(i/2)
#     lst = set(lst)
#     lst = list(lst)
#     return lst
# while True:
#     if X == 1:
#         break
#     temp = result
#     result = []
#     result = calculation(temp)
#     count += 1
#     if min(result) == 1:
#         break
# print(count)

# n = int(input())
# d = [0]*(n+1)
# d[1] = 0
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     if i%2 == 0 and d[i] > d[i//2] + 1:
#         d[i] = d[i//2] + 1
#     if i%3 == 0 and d[i] > d[i//3] + 1:
#         d[i] = d[i//3] + 1
# print(d[n])

def go(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n-1) + 1
    if n%2 == 0:
        temp = go(n//2) + 1 # 나누기(/)로 하면 소수 나와서 오류생김
        if d[n] > temp:
            d[n] = temp
    if n%3 == 0:
        temp = go(n//3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


n = int(input())
d = [0]*(n+1)
print(go(n))