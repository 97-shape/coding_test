from collections import deque

s = deque()
s += list(map(int, input().rstrip()))

a = s.popleft()
while s:
  b = s.popleft()
  print(a, b)
  if a*b > a+b: a = a*b
  else: a = a+b

print(a)