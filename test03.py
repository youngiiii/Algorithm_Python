# 대학생 새내기들의 90 % 는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력 : 첫째 줄에는 테스트 케이스의 개수 C, 
#        둘째 줄부터 각 테스트 케이스마다 학생의 수 
#        이어서 N명의 점수가 주어진다.

# 출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 
# 소수점 셋째 자리까지 출력한다.

#test 케이스 개수
cnt = int(input())

#점수 받아오기
lst = list()
for i in range(cnt):
    lst.append(list(map(int, input().split(" "))))

 
for j in range(0,cnt):
    student = 0
    del lst[j][0] #lst에 첫째자리 수 삭제
    avg = sum(lst[j]) / len(lst[j])  #평균구하기

    for v in lst[j]:
       if(avg < v):
           student += 1

    result = ( student / len(lst[j])) * 100
    print(format(result,".3f") + "%")
                