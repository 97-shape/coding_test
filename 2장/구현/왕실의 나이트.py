x, y = input().strip()
x = ord(x) - (ord("a")-1)  #아스키 코드로 변환 후 좌표 계산
y = int(y)
# 갈 수 있는 방향에 대한 좌표 변화 값
d = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
cnt = 0

for dx, dy in d:
    if 0 < x+dx <= 8 and 0 < y+dy <= 8:
        cnt += 1

print(cnt)