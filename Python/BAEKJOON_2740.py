N, M1 = map(int, input().split())

A = []

for i in range(N):
    element = list(map(int, input().split()))
    A.append(element)

M2, K = map(int, input().split())

B = []

for i in range(M2):
    element = list(map(int, input().split()))
    B.append(element)

if M1 != M2:
    print("행렬 곱셈이 불가능합니다.")

result = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M1):
            result[i][j] += A[i][k] * B[k][j]
            
for i in range(N):
    for j in range(K):
        print(result[i][j], end = " ")
    print()