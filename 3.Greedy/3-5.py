#N, K를 공백으로 구분하여 입력받기 
n, k = map(int, input().split())
result = 0

#N이 K보다 크면 K로 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

    while n>1:
        n -= 1
        result += 1

    print(result)