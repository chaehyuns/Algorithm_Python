#3-5와 동일한 문제이지만 시간복잡도를 낮출 수 있는 테크닉
n, k = map(int, input().split())
result = 0

while True:
    #target을 사용해서 시간 복잡도를 낮춤
    target = (n // k) * k
    result += (n - target)
    n = target
    #n이 k보다 작을 때는 반복문을 나감
    if n < k:
        break
    result += 1
    n //= k

#n<k
result += (n - 1)
print(result)