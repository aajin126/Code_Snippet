chesscheck = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chesscheck1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
N, M = map(int, input().split())
chess = [list(input())for i in range(N)]
count = []
for i in range(N-7):
    for j in range(M-7):
        count1 = 0
        count2 = 0
        check = []
        for k in range(i, i+8):
            list1 = []
            for m in range(j, j+8):
                list1.append(chess[k][m])
            check.append(list1)
        for k in range(8):
            for m in range(8):
                if chesscheck[k][m] != check[k][m]:
                    count1 += 1
                if chesscheck1[k][m] != check[k][m]:
                    count2 += 1
        count.append(count1)
        count.append(count2)
print(min(count))