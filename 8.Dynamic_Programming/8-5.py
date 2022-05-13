#make 1
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    #현재의 수에서 1을 뺴는 경우
    d[i] = d[i-1] + 1 
    #2로 나누어 떨어지는 경우
    if d % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if d % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if d % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])