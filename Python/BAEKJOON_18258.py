from sys import stdin

input()
s, com= [], stdin.readlines() # s로 list 초기화, com에 입력한 명령 저장

cnt = 0 # 숫자가 있는 가장 앞의 인덱스를 가리키는 index

for x in com:
    c = x.split() # 현재 명령어를 저장 
    if c[0] == "push":
        s.append(c[1])
        
    elif c[0] == 'pop': 
        if len(s) > cnt: # cnt값보다 len이 크면 가장 앞의 숫자 print한 후 index 증가
            print(s[cnt])
            cnt += 1
        else:  
            print(-1)
        
    elif c[0] == 'size':
        print(len(s)-cnt)
        
    elif c[0] == 'empty':
        if len(s) == cnt : # empty면 list 초기화 
            print(1)
            cnt = 0
            s = []
        else: 
            print(0)
        
    elif c[0] == 'front':
        if len(s) > cnt: 
            print(s[cnt])
        else: 
            print(-1)
        
    elif c[0] == 'back':
        if len(s) > cnt: 
            print(s[-1])
        else: 
            print(-1)