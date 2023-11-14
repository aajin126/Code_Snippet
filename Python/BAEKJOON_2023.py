'''
#소수 판정 : 1과 자기 자신을 제외한 어떤 수로도 나누어 떨어지지 않는 수
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for num in range(10 ** (n - 1), 10 ** n): # N-1 제곱 ~ N 제곱 자리 수
    if is_prime(num):
        num_str = str(num)
        is_all_prime = True
        for i in range(1, n + 1):
            if not is_prime(int(num_str[:i])):
                    is_all_prime = False
                    break
        if is_all_prime:
            print(num)
        else:
            continue
'''

import sys
input = sys.stdin.readline


n = int(input())

def find(x):
    for i in range(2, int(x**0.5) + 1):
        if int(x) % i == 0:
            return False
    return True


def dfs(num):
    # n 자릿수 도달 시 멈춤
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            # 10 곱하고 i 더해서 자릿수 늘린 수가 소수일때만
            if find(temp):
                dfs(temp)

# 한자리 숫자 중에 소수로 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)