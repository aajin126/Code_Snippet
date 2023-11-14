K = int(input())
visit_order = list(map(int, input().split()))

level_start = 1
level_size = 2 ** (K - 1)

for level in range(K):
    level_buildings = visit_order[level_start - 1:level_start - 1 + level_size]
    print(*level_buildings)
    
    # 다음 레벨의 시작 계산
    level_start = level_start + level_size
    level_size = level_size // 2
