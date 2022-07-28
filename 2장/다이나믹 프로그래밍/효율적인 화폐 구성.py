n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [10001] * (m+1)

dp[0]= 0
# 동전의 수만큼 반복
for c in coin:
    for i in range(c, m+1):
        # 구하고자 하는 금액에서 현재 선택된 동전의 금액을 뺐을 때 동전의 개수와 비교
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)
