import random

# [블록 1] 정답 만들기: 1~9 중 서로 다른 숫자 3개
def make_answer():
    return random.sample(range(1, 10), 3)

# [블록 2] 입력 검사 : 문제가 있으면 안내 문장, 없으면 ""
def check_input(text):
    if len(text) != 3 or not text.isdigit():
        return '세 자리 숫자를 입력하세요.'
    if '0' in text:
        return '0은 쓸 수 없습니다. (1~9만)'
    if len(set(text)) != 3:
        return '서로 다른 숫자 3개를 입력하세요.'
    return ""