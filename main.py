import streamlit as st
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(page_title="기상별 운동 추천", page_icon="🏃", layout="centered")

# CSS 스타일 적용
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
    }
    .exercise-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    .exercise-list {
        background-color: #e6f7ff;
        padding: 10px;
        border-radius: 10px;
        margin-top: 10px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center;'>🏃 기상에 따른 실내·실외 운동 추천</h1>", unsafe_allow_html=True)
st.write("오늘의 날씨에 맞춰 알맞은 운동을 추천해드립니다.")

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

# 카드 형태로 표시
st.markdown("<div class='exercise-card'>", unsafe_allow_html=True)
st.subheader(f"추천 유형: {result['type']}")
st.image(result['image'], use_column_width=True)
st.markdown("<div class='exercise-list'>", unsafe_allow_html=True)
st.write("**추천 운동 목록**")
for ex in result['exercises']:
    st.markdown(f"- {ex}")
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 오늘 날짜
st.caption(f"추천일: {datetime.now().strftime('%Y-%m-%d')}")
