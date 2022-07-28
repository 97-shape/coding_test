n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, start, end):
    result = 0
    while start <= end:
        sum_length = 0
        mid = (start + end) // 2
        # 잘린 떡들의 길이 계산
        for a in arr:
            if a > mid:
                sum_length += a - mid
        #  가능한 적은 떡을 줄 수 있는 경우를 찾기
        if sum_length < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(binary_search(arr, 0, max(arr)))
