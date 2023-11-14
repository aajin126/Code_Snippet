N, M = map(int, input().split())

# 수열을 저장할 리스트 M의 길이 만큼
sequence = [0] * M

# 수열을 생성하는 재귀 함수
def generate_sequence(index):
    if index == M:
        # 수열이 완성되면 출력
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        sequence[index] = i
        generate_sequence(index + 1)

# 재귀 함수 호출
generate_sequence(0)
