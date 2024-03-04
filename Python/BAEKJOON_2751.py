import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arrsorted = sorted(arr)

for i in arrsorted:
        sys.stdout.write(str(i) + "\n")