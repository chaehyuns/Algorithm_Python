
n, m = map(int, input().split())

#맵 생성(초기화)
d = [[0] * m for _ in range(n)]
#캐릭터 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표는 방문처리

#맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#동서남북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1 
turn_time=0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    #네방향 모두 못가는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break

        turn_time=0

print(count)