n = int(input())
k = list(map(int, input().split()))

dp = [0] * n
dp[0] = k[0]
dp[1] = max(k[0], k[1])  # 첫번째 창고를 선택했을떼와 두번째 창고를 선택했을때 가장 큰 값을 기록
for i in range(2, n):
    dp[i] = max(dp[i], dp[i-2]+k[i])

print(dp[n-1])