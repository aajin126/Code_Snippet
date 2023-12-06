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

#초기화        
board = [[0 for _ in range(N)] for _ in range(N)] # board 값 0으로 초기화
board[0][0] = 1 # 뱀이 있는 곳은 1로 flag

end = True
clock = 0
body = [[0,0]] # 몸통이 있는 좌표
head = (0,0) # 머리가 있는 좌표
tail = (0,0) # 꼬리가 있는 좌표

while(end):
    for t in time:
        if t == clock:
            if dir[t] == 'D':
                head[0] += 1
                if len(body) == 1:
                    
                else:
                    

            elif dir[t] == 'L':
                
    clock += 1