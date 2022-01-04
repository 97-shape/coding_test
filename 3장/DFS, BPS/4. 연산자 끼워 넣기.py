import sys
input = sys.stdin.readline

def DFS(v, res, plus, sub, mul, div):
  global max_res, min_res
  if v == n:
    max_res = max(max_res, res)
    min_res = min(min_res, res)
  
  if plus:
    DFS(v+1, res + arr[v], plus - 1, sub, mul, div)
  if sub:
    DFS(v+1, res - arr[v], plus, sub - 1, mul, div)
  if mul:
    DFS(v+1, res * arr[v], plus, sub, mul - 1, div)
  if div:
    DFS(v+1, -(-res // arr[v]) if res < 0 else res // arr[v], plus, sub, mul, div-1)
  

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

max_res = -float('inf')
min_res = float('inf')

DFS(1, arr[0], op[0], op[1], op[2], op[3])
print(max_res)
print(min_res)