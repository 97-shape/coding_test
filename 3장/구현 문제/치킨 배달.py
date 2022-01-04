from itertools import combinations

def city_distance(c):
  res = 0
  for h in house:
    x1, y1 = h
    temp = float('inf')
    for x2, y2 in c:
      temp = min(temp, abs(x2-x1) + abs(y2-y1))
    res += temp
  return res

n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
      if arr[j] == 1: house.append((i, j))
      elif arr[j] == 2: chicken.append((i, j))

C = list(combinations(chicken, m))  # m개의 치킨집을 선택하는 경우

res = float('inf')
for c in C:
  res = min(res, city_distance(c))

print(res)