import streamlit as st
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(page_title="운동 추천 앱", page_icon="🏃", layout="centered")

# 제목
st.title("🏃 기상에 따른 실내·실외 운동 추천")
st.write("오늘 날씨에 맞춰 운동을 추천해드립니다.")

# 날씨 입력
weather = st.selectbox(
    "현재 날씨를 선택하세요:",
    ["맑음", "흐림", "비", "눈", "폭염", "한파"]
)

# 기온 입력
temperature = st.slider("현재 기온 (℃)", -10, 40, 20)

# 운동 추천 로직
def recommend_exercise(weather, temp):
    if weather in ["맑음", "흐림"] and 10 <= temp <= 28:
        return {
            "type": "실외 운동",
            "exercises": ["조깅", "자전거 타기", "등산", "파워워킹"],
            "image": "https://cdn.pixabay.com/photo/2016/11/29/01/54/runner-1867053_1280.jpg"
        }
    elif weather in ["비", "눈"] or temp < 10 or temp > 28:
        return {
            "type": "실내 운동",
            "exercises": ["요가", "러닝머신", "홈트레이닝", "필라테스"],
            "image": "https://cdn.pixabay.com/photo/2017/03/23/10/11/yoga-2162954_1280.jpg"
        }
    elif weather == "폭염":
        return {
            "type": "실내 운동",
            "exercises": ["수영", "실내 자전거", "에어로빅"],
            "image": "https://cdn.pixabay.com/photo/2017/08/06/13/48/swimming-2598420_1280.jpg"
        }
    elif weather == "한파":
        return {
            "type": "실내 운동",
            "exercises": ["스트레칭", "실내 근력운동"],
            "image": "https://cdn.pixabay.com/photo/2017/06/17/18/31/training-2415746_1280.jpg"
        }
    else:
        return {
            "type": "실내 운동",
            "exercises": ["가벼운 스트레칭"],
            "image": "https://cdn.pixabay.com/photo/2017/01/13/20/21/stretching-1973478_1280.jpg"
        }

# 추천 결과
result = recommend_exercise(weather, temperature)

# 결과 표시
st.subheader(f"추천 유형: {result['type']}")
st.image(result['image'], use_column_width=True)
st.write("추천 운동:")
for ex in result['exercises']:
    st.markdown(f"- {ex}")

# 오늘 날짜
st.caption(f"추천일: {datetime.now().strftime('%Y-%m-%d')}")
