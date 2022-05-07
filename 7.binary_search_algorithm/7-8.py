#떡의 개수와 요정한 떡의 길이 입력받기
n,m = list(map(int, input().split(' ')))
#각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

#이진탐샏을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진탐색 수행
result = 0
while(start <= end):
    total = 0
    mid = (start + end) //2 
    for x in array:
        #잘랐을 떄 떡의 양 계산
        if x > mid :
            total += x - mid
        #떡의 양이 부족한 경우 더 많이 자르기
        if total < m:
            end = mid - 1
        #떡의 양이 충분한 경우 덜 자르기
        else: 
            result = mid #최대한 덜 잘렸을 때가 정답이므로 여기에 result 저장
            start = mid + 1
#정답
print(result)