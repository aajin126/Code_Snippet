list_house = []
end_list = []

for a in range(15):
    list_house.append(list(range(1, 16)))
    
for i in range(1, 15):
    for j in range(0, 15):
        people_sum = 0
        for k in range(0, j + 1):
            people_sum += list_house[i - 1][k]
        list_house[i][j] = people_sum

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input()) - 1
    if n == -1:
        n = 0
    print(list_house[k][n])