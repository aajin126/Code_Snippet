# 떡의 개수 : N, 요청한 떡의 길이: M
N, M = map(int, input().split())
#N개의 떡의 길이들
numbers = list(map(int, input().split()))

max_num = max(numbers)

for j in range(max_num, 0,-1):
    
    results = [0] * N
    total = 0
    
    for i in range(N):
        if numbers[i] < j:
            results[i] = 0
        else:
            results[i] = numbers[i]
            

    # 리스트의 모든 요소를 더하기
    for num in results:
        total += num    
    
    if total >= M:
        result = j
        break

print(result)

