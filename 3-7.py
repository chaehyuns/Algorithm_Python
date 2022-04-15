#곱하기 혹은 더학기 문제
#0뿐만 아니라 1인 경우에도 +를 하는게 유리한것을 유의해야함.
data = input()

#  문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

#입력받는 방법이 바로 생각나지 않고 첫번째 숫자가 0,1인 경우를 놓쳤었다. 다방면에서 생각을 해야할 필요성을 느낌 