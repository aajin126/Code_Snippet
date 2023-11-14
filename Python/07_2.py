N = int(input())

N_numbers = list(map(int, input().split()))

M = int(input())

M_numbers = list(map(int, input().split()))

for i in range(M):
    if M_numbers[i] in N_numbers:
        print("yes", end = ' ')
    elif M_numbers[i] not in N_numbers:
        print("no", end = ' ')