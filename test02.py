#"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.

#"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

#입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 문자열은 O와 X만으로 이루어져 있다.

#출력 : 각 테스트 케이스마다 점수를 출력한다.

#테스트 케이스 개수
cnt = int(input()) 

#문자열 입력받아오기
lst = list()
for i in range(cnt):
    lst.append(str(input()))
    
#점수 출력
for i in range(cnt):
    goal = 0
    addNum = 1
    for j in range(len(lst[i])):
        if lst[i][j] == 'O':
            goal += addNum
            addNum += 1
        else:
            addNum = 1
    print(goal)
    goal = 0
    addNum = 1

