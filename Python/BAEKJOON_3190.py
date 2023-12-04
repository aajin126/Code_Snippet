N = int(input())
K = int(input())

apple = []

for i in range(K):
    for j in range(1):
        pos = list(map(int, input().split()))
        apple.append(pos)

L = int(input())

time = []
dir = []

for k in range(L):
    for j in range(1):
        temp = list(map(input().split()))
        time.append(int(temp[k][0]))
        dir.append(temp[k][1])

