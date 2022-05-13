#개미전사
n = int(input())
#식량 정보 입력받기
array = list(map(int, input().split()))

#dp테이블 초기화
d = [0] * 100

#다이나믹 프로그밍 보텀업 방식
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n+1):
    d[i] = max(d[i-1], d[i-2] + array[i])

#출력
print(d[n-1])