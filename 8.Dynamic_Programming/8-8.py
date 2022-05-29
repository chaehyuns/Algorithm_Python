#정수 n과 m을 입력받기  
n, m = map(int, input().split())
#화폐 정보 입력받기
array =[]
for i in range(n):
    array.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP테이블
d = [1001] * (m+1)

#다이나믹 프로그래밍 진행 - 보텀업
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 1001:
            d[j] = min(d[j], d[j- array[i]] + 1)
#계산된 결과 출력
if d[m]  == 1001:
    print(-1)
else :
    print(d[m])