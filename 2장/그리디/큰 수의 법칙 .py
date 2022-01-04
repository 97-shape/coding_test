n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

f = arr[0]
s = arr[1]

res = (f * k +s) * (m // (k+1)) + f * (m % (k+1))
print(res)