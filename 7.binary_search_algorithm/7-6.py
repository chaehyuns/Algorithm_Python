#계수 정렬을 사용(소스코드 간결)
n = int(input())
array = [0] * 100001

#가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

#손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = input(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부분이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')