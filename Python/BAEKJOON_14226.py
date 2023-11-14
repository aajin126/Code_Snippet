from collections import deque

def min_time_to_get_emojis(S):
    # dp[i][j]는 화면에 i개의 이모티콘이 있고 클립보드에 j개의 이모티콘이 있을 때의 최소 시간
    dp = [[-1] * (S + 1) for _ in range(S + 1)]

    q = deque()
    q.append((1, 0))  # 초기 상태: 화면에 1개의 이모티콘, 클립보드에 0개의 이모티콘

    dp[1][0] = 0  # 초기 상태의 시간은 0

    while q:
        screen, clipboard = q.popleft()

        # 1. 클립보드에 현재 화면에 있는 이모티콘을 복사
        if dp[screen][screen] == -1:
            dp[screen][screen] = dp[screen][clipboard] + 1
            q.append((screen, screen))

        # 2. 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if screen + clipboard <= S and dp[screen + clipboard][clipboard] == -1:
            dp[screen + clipboard][clipboard] = dp[screen][clipboard] + 1
            q.append((screen + clipboard, clipboard))

        # 3. 화면에 있는 이모티콘 중 하나 삭제
        if screen > 1 and dp[screen - 1][clipboard] == -1:
            dp[screen - 1][clipboard] = dp[screen][clipboard] + 1
            q.append((screen - 1, clipboard))

    # 화면에 S개의 이모티콘을 만드는데 걸리는 최소 시간을 반환
    return min(dp[S])

S = int(input())
result = min_time_to_get_emojis(S)
print(result)
