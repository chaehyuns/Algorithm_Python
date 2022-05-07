#이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점보다 작은 경우
        elif array[mid] > target:
            end = mid - 1
        #중간점보다 큰 경우
        else:
            start = mid + 1
    return None

#N개수 입력
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

#부품 번호 하나씩 확인
for i in x:
    #해당 부품이 있는지 없는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('No', end = ' ')