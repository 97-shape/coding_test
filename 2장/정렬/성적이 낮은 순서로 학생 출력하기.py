n = int(input())

arr = []
for i in range(n):
    name, grade = input().split()
    arr.append([name, int(grade)])

arr.sort(key= lambda x: x[1])

for a in arr:
    print(a[0], end=' ')