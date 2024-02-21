N = int(input())

score = list(map(int, input().split()))

max_score = max(score)

score = list(map(lambda a : a / max_score * 100, score))

print(sum(score) / N)