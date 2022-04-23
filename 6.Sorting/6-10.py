#N입력
n = int(input())
array = []
#N개의 정수를 입력받아 리스트에 저장
for i in range(n):
    array.append(int(input()))

#내림차순으로 sort
array = sorted(array, reverse=True)

#정렬이 수행된 결과 출력
for i in array:
    print(i, end=' ')