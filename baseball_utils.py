import random

# [블록 1] 정답 만들기: 1~9 중 서로 다른 숫자 3개
def make_answer():
    return random.sample(range(1, 10), 3)