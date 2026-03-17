import html

# 이 코드는 파일 경로를 다루기 위한 기능을 불러오는 역할을 합니다.
import os

# 이 코드는 파이썬이 다른 폴더의 파일도 찾을 수 있게 도와주는 기능을 불러오는 역할을 합니다.
import sys


# 이 코드는 현재 파일(main_app.py) 기준으로 프로젝트의 가장 바깥 폴더 경로를 찾는 역할을 합니다.
# 예를 들어 src/app/main_app.py 에서 두 단계 위로 올라가면 프로젝트 루트 폴더가 됩니다.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# 이 코드는 파이썬이 src 폴더 안의 모듈들을 잘 찾을 수 있도록,
# 프로젝트 루트 경로를 sys.path 목록에 추가하는 역할을 합니다.
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# 이 코드는 표 형태 데이터(DataFrame)를 다루기 위한 pandas를 불러오는 역할을 합니다.
import pandas as pd

# 이 코드는 웹 화면(Streamlit 앱)을 만들기 위한 streamlit을 불러오는 역할을 합니다.
import streamlit as st


# 이 코드는 환경설정 파일(settings.py)에 들어 있는 카카오 API 관련 설정값을 불러오는 역할을 합니다.
# 현재 main_app.py에서 직접 사용하지는 않지만, 프로젝트 전체 설정을 맞출 때 참고용으로 남아 있습니다.
from src.config.settings import KAKAO_REST_API_KEY, KAKAO_JAVASCRIPT_KEY


# 이 코드는 각 메뉴에서 사용할 데이터를 불러오는 함수들을 가져오는 역할을 합니다.
# 쉽게 말하면, 앱에 필요한 재료들을 준비하는 함수들을 한 번에 가져오는 부분입니다.
from src.db.query_data import (
    load_charger_operation_data,
    load_charging_fee_data,
    load_ev_registration_data,
    load_faq_data,
    load_news_keyword_data,
    load_policy_data,
    load_brand_faq_data,
)

# 이 코드는 1번 메뉴 '지역 별 전기차 등록 현황' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.region_ev_section import render_region_ev_page

# 이 코드는 2번 메뉴 '충전소 위치 / 충전 가능 여부 / 운영 정보' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.charger_section import render_charger_page

# 이 코드는 3번 메뉴 '충전 요금 관련' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.charging_fee_section import render_charging_fee_page

# 이 코드는 4번 메뉴 '보조금 정책' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.subsidy_section import render_subsidy_page

# 이 코드는 7번 메뉴 '브랜드 전기차 FAQ' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.brand_faq_section import render_brand_faq_page

# 이 코드는 6번 메뉴 '서울시 전기차 FAQ' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.faq_section import render_faq_page

# 이 코드는 7번 메뉴 '뉴스 기사 분석' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.news_analysis_section import render_news_page


# 이 코드는 왼쪽 메뉴에 보여줄 1번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_REGION_EV = "지역별 전기차 등록 현황"

# 이 코드는 왼쪽 메뉴에 보여줄 2번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_CHARGER = "전기차 충전소 정보"

# 이 코드는 왼쪽 메뉴에 보여줄 3번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_CHARGING_FEE = "충전 요금 정보"

# 이 코드는 왼쪽 메뉴에 보여줄 4번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_SUBSIDY = "보조금 정책"

# 이 코드는 왼쪽 메뉴에 보여줄 5번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_BRAND_FAQ = "브랜드별 전기차 FAQ"

# 이 코드는 왼쪽 메뉴에 보여줄 6번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_FAQ = "서울시 전기차 FAQ"

# 이 코드는 왼쪽 메뉴에 보여줄 7번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_NEWS = "뉴스 기사 분석"


# 이 코드는 앱에서 필요한 데이터를 한 번에 불러오는 역할을 합니다.
# @st.cache_data 는 같은 데이터를 계속 다시 읽지 않도록 저장해두는 역할을 합니다.
# 그래서 메뉴를 바꿀 때 조금 더 빠르게 동작할 수 있습니다.
@st.cache_data(show_spinner=False)
def load_dashboard_data():
    # 이 코드는 각 메뉴별로 필요한 데이터를 딕셔너리 형태로 모아서 돌려주는 역할을 합니다.
    # 예를 들어 1번 메뉴용 데이터, 2번 메뉴용 데이터, 3번 메뉴용 데이터를 한 번에 준비합니다.
    return {
        "ev_registration_data": load_ev_registration_data(),
        "charger_operation_data": load_charger_operation_data(),
        "charging_fee_data": load_charging_fee_data(),
        "policy_data": load_policy_data(),
        "faq_data": load_faq_data(),
        "news_keyword_data": load_news_keyword_data(),
        "brand_faq_data": load_brand_faq_data(),
    }


# 이 코드는 화면 왼쪽에 보이는 사이드바 메뉴를 만드는 역할을 합니다.
def render_sidebar() -> str:
    # 이 코드는 Streamlit의 사이드바 영역 안에 내용을 넣겠다는 뜻입니다.
    with st.sidebar:
        # 이 코드는 왼쪽 사이드바의 큰 제목을 보여주는 역할을 합니다.
        st.title("⚡ EV 정보 포털")

        # 이 코드는 사이드바 제목 아래에 짧은 설명 문장을 보여주는 역할을 합니다.
        st.caption("메뉴를 선택하면 전기차 관련 정보를 확인할 수 있습니다.")

        # 이 코드는 사용자가 1번~6번 메뉴 중 하나를 고를 수 있게 하는 라디오 버튼을 만드는 역할을 합니다.
        selected_menu = st.radio(
            "메뉴 선택",
            [
                MENU_REGION_EV,
                MENU_CHARGER,
                MENU_CHARGING_FEE,
                MENU_SUBSIDY,
                MENU_BRAND_FAQ,
                MENU_FAQ,
                MENU_NEWS,
            ],
            label_visibility="collapsed",
        )

    # 이 코드는 사용자가 고른 메뉴 이름을 main 함수로 돌려주는 역할을 합니다.
    return selected_menu


# 이 코드는 이 앱 전체를 실제로 실행하는 가장 중요한 함수 역할을 합니다.
def main() -> None:
    # 이 코드는 Streamlit 웹페이지의 기본 설정을 정하는 역할을 합니다.
    # 브라우저 탭 제목, 아이콘, 화면 넓이 등을 여기서 정합니다.
    st.set_page_config(page_title="전기차 정보 포털", page_icon="⚡", layout="wide")

    # 이 코드는 웹페이지 맨 위에 큰 제목을 보여주는 역할을 합니다.
    st.title("전기차 정보 포털")
    
    # 이 코드는 왼쪽 메뉴판을 그리고, 사용자가 어떤 메뉴를 골랐는지 받아오는 역할을 합니다.
    selected_menu = render_sidebar()

    # 이 코드는 각 메뉴에서 사용할 데이터를 한 번에 준비해두는 역할을 합니다.
    dashboard_data = load_dashboard_data()

    # 이 코드는 사용자가 선택한 메뉴에 따라 알맞은 화면을 보여주는 역할을 합니다.
    # 쉽게 말하면, '어느 페이지를 보여줄지 결정하는 교통정리' 역할입니다.
    if selected_menu == MENU_REGION_EV:
        # 이 코드는 1번 메뉴가 선택되었을 때 지역 별 전기차 등록 현황 화면을 보여주는 역할을 합니다.
        render_region_ev_page(dashboard_data["ev_registration_data"])

    elif selected_menu == MENU_CHARGER:
        # 이 코드는 2번 메뉴가 선택되었을 때 충전소 위치 / 충전 가능 여부 / 운영 정보 화면을 보여주는 역할을 합니다.
        render_charger_page(dashboard_data["charger_operation_data"])

    elif selected_menu == MENU_CHARGING_FEE:
        # 이 코드는 3번 메뉴가 선택되었을 때 충전 요금 관련 화면을 보여주는 역할을 합니다.
        render_charging_fee_page(dashboard_data["charging_fee_data"])

    elif selected_menu == MENU_SUBSIDY:
        # 이 코드는 4번 메뉴가 선택되었을 때 보조금 정책 화면을 보여주는 역할을 합니다.
        render_subsidy_page(dashboard_data["policy_data"])

        # 이 코드는 5번 메뉴가 선택되었을 때 브랜드 전기차 FAQ 화면을 보여주는 역할을 합니다.
    elif selected_menu == MENU_BRAND_FAQ:
        render_brand_faq_page(dashboard_data["brand_faq_data"])

    elif selected_menu == MENU_FAQ:
        # 이 코드는 6번 메뉴가 선택되었을 때 서울시 전기차 FAQ 화면을 보여주는 역할을 합니다.
        render_faq_page(dashboard_data["faq_data"])

    else:
        # 이 코드는 위의 1~6번 메뉴가 아니라면,
        # 마지막 7번 메뉴인 뉴스 기사 분석 화면을 보여주는 역할을 합니다.
        render_news_page(dashboard_data["news_keyword_data"])


# 이 코드는 이 파일을 직접 실행했을 때 main() 함수를 시작하는 역할을 합니다.
# 쉽게 말하면 "이 파일이 프로그램의 출발점입니다" 라는 뜻입니다.
if __name__ == "__main__":
    main()