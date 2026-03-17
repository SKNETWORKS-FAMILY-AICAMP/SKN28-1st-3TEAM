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
    load_local_subsidy_data,
)

# 이 코드는 1번 메뉴 '지역 별 전기차 등록 현황' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.region_ev_section import render_region_ev_page

# 이 코드는 2번 메뉴 '충전소 위치 / 충전 가능 여부 / 운영 정보' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.charger_section import render_charger_page

# 이 코드는 3번 메뉴 '충전 요금 관련' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.charging_fee_section import render_charging_fee_page

# 이 코드는 4번 메뉴 '국고 보조금 정책' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.subsidy_section import render_subsidy_page

# 이 코드는 7번 메뉴 '브랜드 전기차 FAQ' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.brand_faq_section import render_brand_faq_page

# 이 코드는 6번 메뉴 '서울시 전기차 FAQ' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.faq_section import render_faq_page

# 이 코드는 7번 메뉴 '뉴스 기사 분석' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.news_analysis_section import render_news_page

# 이 코드는 4번 추가 메뉴 '지 자체 보조금 정책' 화면을 그리는 함수를 가져오는 역할을 합니다.
from src.data.local_subsidy_section import render_local_subsidy_page


# 이 코드는 왼쪽 메뉴에 보여줄 1번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_REGION_EV = "지역별 전기차 등록 현황"

# 이 코드는 왼쪽 메뉴에 보여줄 2번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_CHARGER = "전기차 충전소 정보"

# 이 코드는 왼쪽 메뉴에 보여줄 3번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_CHARGING_FEE = "충전 요금 정보"

# 이 코드는 왼쪽 메뉴에 보여줄 4번 메뉴 이름을 저장해두는 역할을 합니다.
MENU_SUBSIDY = "보조금 정책"
SUBMENU_NATIONAL_SUBSIDY = "국고 보조금 정책"
SUBMENU_LOCAL_SUBSIDY = "지자체 보조금 정책"

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
        "local_subsidy_data": load_local_subsidy_data(),
        "faq_data": load_faq_data(),
        "news_keyword_data": load_news_keyword_data(),
        "brand_faq_data": load_brand_faq_data(),
    }
def initialize_menu_state() -> None:
    if "current_menu" not in st.session_state:
        st.session_state.current_menu = MENU_REGION_EV

    if "current_submenu" not in st.session_state:
        st.session_state.current_submenu = None

    if "subsidy_expanded" not in st.session_state:
        st.session_state.subsidy_expanded = False

# 이 코드는 화면 왼쪽에 보이는 사이드바 메뉴를 만드는 역할을 합니다.
def render_sidebar() -> tuple[str, str | None]:
    initialize_menu_state()

    def select_main_menu(menu_name: str) -> None:
        st.session_state.current_menu = menu_name
        st.session_state.current_submenu = None

        if menu_name != MENU_SUBSIDY:
            st.session_state.subsidy_expanded = False

    def toggle_subsidy_menu() -> None:
        st.session_state.subsidy_expanded = not st.session_state.subsidy_expanded

    def select_submenu(submenu_name: str) -> None:
        st.session_state.current_menu = MENU_SUBSIDY
        st.session_state.current_submenu = submenu_name
        st.session_state.subsidy_expanded = True

    with st.sidebar:
        st.title("⚡ EV 정보 포털")
        st.caption("메뉴를 선택하면 전기차 관련 정보를 확인할 수 있습니다.")

        if st.button("지역별 전기차 등록 현황", use_container_width=True, key="menu_region_ev"):
            select_main_menu(MENU_REGION_EV)

        if st.button("전기차 충전소 정보", use_container_width=True, key="menu_charger"):
            select_main_menu(MENU_CHARGER)

        if st.button("충전 요금 정보", use_container_width=True, key="menu_charging_fee"):
            select_main_menu(MENU_CHARGING_FEE)

        subsidy_label = "▼ 보조금 정책" if st.session_state.subsidy_expanded else "▶ 보조금 정책"
        if st.button(subsidy_label, use_container_width=True, key="menu_subsidy"):
            toggle_subsidy_menu()

        if st.session_state.subsidy_expanded:
            st.markdown(
                """
                <div style="margin-left: 18px; margin-top: 2px; margin-bottom: 6px;">
                </div>
                """,
                unsafe_allow_html=True,
            )

            sub_col_1, sub_col_2 = st.columns([0.08, 0.92])

            with sub_col_2:
                if st.button("국고 보조금 정책", use_container_width=True, key="submenu_national_subsidy"):
                    select_submenu(SUBMENU_NATIONAL_SUBSIDY)

                if st.button("지자체 보조금 정책", use_container_width=True, key="submenu_local_subsidy"):
                    select_submenu(SUBMENU_LOCAL_SUBSIDY)

        if st.button("브랜드별 전기차 FAQ", use_container_width=True, key="menu_brand_faq"):
            select_main_menu(MENU_BRAND_FAQ)

        if st.button("서울시 전기차 FAQ", use_container_width=True, key="menu_faq"):
            select_main_menu(MENU_FAQ)

        if st.button("뉴스 기사 분석", use_container_width=True, key="menu_news"):
            select_main_menu(MENU_NEWS)

    return st.session_state.current_menu, st.session_state.current_submenu


# 이 코드는 이 앱 전체를 실제로 실행하는 가장 중요한 함수 역할을 합니다.
def main() -> None:
    st.set_page_config(page_title="전기차 정보 포털", page_icon="⚡", layout="wide")
    st.title("전기차 정보 포털")

    current_menu, current_submenu = render_sidebar()
    dashboard_data = load_dashboard_data()

    if current_menu == MENU_REGION_EV:
        render_region_ev_page(dashboard_data["ev_registration_data"])

    elif current_menu == MENU_CHARGER:
        render_charger_page(dashboard_data["charger_operation_data"])

    elif current_menu == MENU_CHARGING_FEE:
        render_charging_fee_page(dashboard_data["charging_fee_data"])

    elif current_menu == MENU_SUBSIDY:
        if current_submenu == SUBMENU_NATIONAL_SUBSIDY:
            render_subsidy_page(dashboard_data["policy_data"])
        elif current_submenu == SUBMENU_LOCAL_SUBSIDY:
            render_local_subsidy_page(dashboard_data["local_subsidy_data"])
        else:
            # 부모 메뉴만 눌렀을 때는 기존 화면 유지
            pass

    elif current_menu == MENU_BRAND_FAQ:
        render_brand_faq_page(dashboard_data["brand_faq_data"])

    elif current_menu == MENU_FAQ:
        render_faq_page(dashboard_data["faq_data"])

    elif current_menu == MENU_NEWS:
        render_news_page(dashboard_data["news_keyword_data"])


# 이 코드는 이 파일을 직접 실행했을 때 main() 함수를 시작하는 역할을 합니다.
# 쉽게 말하면 "이 파일이 프로그램의 출발점입니다" 라는 뜻입니다.
if __name__ == "__main__":
    main()