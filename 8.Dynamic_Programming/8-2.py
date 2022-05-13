#피보나치수열 메모나이제이션(캐싱) 방법 사용
#한 번 계산된 결과값을 저장
d = [0] * 100

#탑다운 다이나믹 프로그래밍
def fibo(x):
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99)) 