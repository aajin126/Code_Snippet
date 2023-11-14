def maximum_volume(N, S, M, volumes):
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = True  # 시작 볼륨 S에서 출발

    for i in range(1, N + 1):
        for j in range(M + 1):
            if not dp[i - 1][j]:
                continue
            if j - volumes[i - 1] >= 0:
                dp[i][j - volumes[i - 1]] = True
            if j + volumes[i - 1] <= M:
                dp[i][j + volumes[i - 1]] = True

    last_volume = -1
    for volume in range(M, -1, -1):
        if dp[N][volume]:
            last_volume = volume
            break

    return last_volume

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))
result = maximum_volume(N, S, M, volumes)

if result == -1:
    print(-1)
else:
    print(result)
