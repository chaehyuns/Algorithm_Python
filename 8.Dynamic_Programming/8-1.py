#피보나치 수열 재귀함수
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))