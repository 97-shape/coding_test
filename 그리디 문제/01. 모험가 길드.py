n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
i = 0
while i < n:
  print(i)
  a = arr[i]
  temp = arr[i: i+a]
  if sum(temp) // a == a:
    print(temp)
    cnt += 1
  i += a

print(cnt)