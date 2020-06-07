
#문제
#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
#등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
#한수의 개수를 출력하는 프로그램을 작성하시오. 

#입력 : 자연수 N이 주어진다.
#출력 : 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def checkNum(num):

    check = True

    #각 자리수의 차수 저장
    lst = list()
    for i in range(1, len(str(num))):
        num1 = int(str(num)[i])
        num2 = int(str(num)[i - 1])
        lst.append(num1 - num2)
    
    #각 자리수 비교
    checkTmp = 0
    for i in range(0,len(lst)):
        if i == 0: checkTmp = lst[i]
        
        if checkTmp != lst[i]: 
            check = False
            break

    return check
        

#자연수 입력
a = int(input())

#99이하 수는 모두 한수
if a < 100:
    print(a)
else:
    cnt = 99 #99이하는 모두 한수이기 때문에
    for i in range(100,a + 1):
        #한수인지 아닌지 Check
        if checkNum(i):
            cnt += 1

    print(cnt)