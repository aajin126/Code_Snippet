# N과 M을 입력으로 받습니다.
# 입력을 받아서 공백을 기준으로 문자열을 나눈 후, 
# 나눠진 각 문자열을 정수로 변환한 뒤, 그 결과를 순서대로 저장하는 코드
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
        if i not in sequence:
            sequence[index] = i
            generate_sequence(index + 1)
            sequence[index] = 0

# 재귀 함수 호출
generate_sequence(0)

