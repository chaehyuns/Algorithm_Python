#집합 자료형 이용방법, 소스코드 간결
n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    #해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')