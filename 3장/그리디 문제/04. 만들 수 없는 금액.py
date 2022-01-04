import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
c.sort()

target = 1
for x in c:
  print(target, x)
  if target < x: break
  target += x

print(target)