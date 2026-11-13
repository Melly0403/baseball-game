import streamlit as st
from baseball_utils import make_answer, check_input, to_numbers, count_strike, count_ball, result_text

st.title('⚾ 숫자야구 게임')
st.markdown('1부터 9까지의 서로 다른 숫자 3개를 맞혀보세요! (중복 없음, 0 불가)')

# 세션 스테이트 초기화
if 'answer' not in st.session_state:
    st.session_state.answer = make_answer()
    st.session_state.tries = 0
    st.session_state.history = []
    st.session_state.done = False

# 새 게임 버튼
def reset_game():
    st.session_state.answer = make_answer()
    st.session_state.tries = 0
    st.session_state.history = []
    st.session_state.done = False

st.button('새 게임 시작', on_click=reset_game)

# 게임이 끝나지 않았을 때만 입력 폼 표시
if not st.session_state.done:
    with st.form('guess_form', clear_on_submit=True):
        user_input = st.text_input('3자리 숫자 입력:', max_chars=3)
        submitted = st.form_submit_button('제출')
        
        if submitted:
            # 입력 검사
            err = check_input(user_input)
            if err != "":
                st.error(err)
            else:
                st.session_state.tries += 1
                guess = to_numbers(user_input)
                strike = count_strike(st.session_state.answer, guess)
                ball = count_ball(st.session_state.answer, guess)
                msg = result_text(strike, ball)
                
                # 기록 저장
                st.session_state.history.append((user_input, msg))
                
                # 3스트라이크 성공 시
                if strike == 3:
                    st.session_state.done = True

# 결과 출력
if st.session_state.done:
    st.success(f'🎉 축하합니다! 총 {st.session_state.tries}번 만에 맞혔습니다!')
    st.balloons()

# 시도 기록 보여주기
if st.session_state.history:
    st.subheader('📝 시도 기록')
    for idx, (g, m) in enumerate(st.session_state.history, 1):
        st.write(f'{idx}회차] 입력: {g} → 결과: {m}')