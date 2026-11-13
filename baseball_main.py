from baseball_utils import *

print('=== 숫자야구 게임 (콘솔 버전) ===')
answer = make_answer()
tries = 0

while True:
    text = input('3자리 숫자 입력 (예: 472): ')
    
    # 입력 검사
    err = check_input(text)
    if err != "":
        print(err)
        continue
        
    tries += 1
    guess = to_numbers(text)
    
    # 스트라이크, 볼 판정
    strike = count_strike(answer, guess)
    ball = count_ball(answer, guess)
    msg = result_text(strike, ball)
    
    print(f'결과: {msg}')
    
    # 3스트라이크면 게임 종료
    if strike == 3:
        print(f'축하합니다! {tries}번 만에 맞혔습니다.')
        break