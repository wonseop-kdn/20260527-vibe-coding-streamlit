import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="임원섭 | 포트폴리오",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container { padding-top: 2rem; padding-bottom: 2rem; }

    .main-heading {
        font-size: 2.5rem; font-weight: 800;
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; margin-bottom: 0.5rem;
    }
    .sub-heading { font-size: 1.1rem; color: #64748b; margin-bottom: 1.5rem; }

    .stat-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        border-radius: 16px; padding: 1.5rem; color: white; text-align: center;
    }
    .stat-number { font-size: 2.5rem; font-weight: 800; margin: 0; line-height: 1; }
    .stat-label { font-size: 0.9rem; opacity: 0.85; margin: 0.25rem 0 0 0; }

    .project-card {
        border: 1px solid #e2e8f0; border-radius: 16px; padding: 1.5rem;
        background: #ffffff; box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin-bottom: 1.5rem; border-left: 4px solid;
    }
    .project-title { font-size: 1.3rem; font-weight: 700; margin: 0 0 0.75rem 0; }
    .project-desc { color: #4b5563; line-height: 1.6; margin-bottom: 1rem; }

    .tag {
        display: inline-block; background: #dbeafe; color: #1e40af;
        padding: 0.2rem 0.65rem; border-radius: 9999px;
        font-size: 0.75rem; font-weight: 600; margin: 0.15rem;
    }
    .cert-box {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border: 1px solid #f59e0b; border-radius: 12px;
        padding: 1rem 1.5rem; margin-bottom: 1rem;
    }
    .cert-name { font-size: 1.1rem; font-weight: 700; color: #92400e; margin: 0 0 0.25rem 0; }
    .cert-info { font-size: 0.85rem; color: #78350f; margin: 0; }

    .timeline-container {
        border-left: 3px solid #3b82f6; padding-left: 1.5rem; margin-left: 0.5rem;
    }
    .skill-label { display: flex; justify-content: space-between; margin-bottom: 0.25rem; }

    .interest-tag {
        display: inline-block; background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        color: #1e40af; padding: 0.4rem 1rem; border-radius: 9999px;
        font-size: 0.9rem; font-weight: 600; margin: 0.3rem;
        border: 1px solid #93c5fd;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f0f4ff 0%, #ffffff 100%);
    }
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "profile_img" not in st.session_state:
    st.session_state.profile_img = None

# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:1rem 0 0.5rem;">
        <p style="font-size:1.4rem; font-weight:800; color:#1e3a8a; margin:0;">⚡ 임원섭</p>
        <p style="font-size:0.85rem; color:#64748b; margin:0.25rem 0;">한전KDN | 계통제어부</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "프로필 사진 업로드",
        type=["jpg", "jpeg", "png"],
        help="JPG 또는 PNG 파일을 업로드하세요"
    )
    if uploaded:
        img = Image.open(uploaded)
        w, h = img.size
        size = min(w, h)
        img = img.crop(((w - size) // 2, (h - size) // 2, (w + size) // 2, (h + size) // 2))
        img = img.resize((200, 200))
        st.session_state.profile_img = img

    if st.session_state.profile_img:
        st.image(st.session_state.profile_img, use_container_width=True)
    else:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1e3a8a,#3b82f6);
                    width:100%; aspect-ratio:1/1; border-radius:12px;
                    display:flex; align-items:center; justify-content:center;
                    font-size:5rem; text-align:center; padding:1rem; box-sizing:border-box;">
            👤
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    page = st.radio(
        "페이지",
        ["🏠  홈", "👤  소개", "📋  경력 & 자격증", "🔧  프로젝트"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.8rem; color:#94a3b8; text-align:center; line-height:1.8;">
        📧 wonseob_123@kdn.com<br>
        🏢 계통제어부
    </div>
    """, unsafe_allow_html=True)


# ─── HOME ────────────────────────────────────────────────────────────────────
if "홈" in page:
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown('<h1 class="main-heading">안녕하세요!<br>임원섭입니다 👋</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-heading">한전KDN 계통제어부 · 전기직렬 엔지니어</p>', unsafe_allow_html=True)
        st.markdown("""
        전력 계통의 **안정적인 운영**과 **미래 기술**을 연구하는 엔지니어입니다.

        전기 분야의 전문 지식을 바탕으로 SPS 고장파급방지시스템, 변전소 자동화,
        정보전송장치 분야에서 다수의 사업을 수행하였으며, 현재는 **AI와 데이터 기술**을
        전력계통에 접목하는 연구에 집중하고 있습니다.
        """)
        st.markdown("#### 관심 분야")
        st.markdown("""
        <div>
            <span class="interest-tag">⚡ 전력계통</span>
            <span class="interest-tag">🤖 AI / 머신러닝</span>
            <span class="interest-tag">📊 데이터 분석</span>
            <span class="interest-tag">🔌 변전소 자동화</span>
            <span class="interest-tag">🛡️ 고장파급방지</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.session_state.profile_img:
            large = st.session_state.profile_img.resize((300, 300))
            st.image(large, use_container_width=True)
        else:
            st.markdown("""
            <div style="background:linear-gradient(135deg,#1e3a8a,#3b82f6);
                        border-radius:20px; padding:3rem; text-align:center; font-size:6rem;">
                ⚡
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip(
        [c1, c2, c3, c4],
        [("3+", "수행 프로젝트"), ("2", "보유 자격증"), ("4+", "경력 (년)"), ("∞", "성장 의지")]
    ):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{num}</p>
                <p class="stat-label">{label}</p>
            </div>
            """, unsafe_allow_html=True)


# ─── ABOUT ───────────────────────────────────────────────────────────────────
elif "소개" in page:
    st.markdown("## 👤 소개")
    st.markdown("---")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 기본 정보")
        for label, value in [
            ("이름", "임원섭"),
            ("소속", "한전KDN"),
            ("부서", "계통제어부"),
            ("직렬", "전기직렬"),
            ("관심분야", "AI, 데이터, 전력계통"),
            ("이메일", "wonseob_123@kdn.com"),
        ]:
            c_l, c_v = st.columns([1, 2])
            c_l.markdown(f"**{label}**")
            c_v.markdown(value)

    with col2:
        st.markdown("### 기술 역량")
        for skill, pct in [
            ("전력계통 분석", 90),
            ("변전소 시스템", 85),
            ("데이터 분석", 75),
            ("AI / 머신러닝", 70),
            ("파이썬 프로그래밍", 68),
        ]:
            st.markdown(f"""
            <div class="skill-label">
                <span><b>{skill}</b></span>
                <span style="color:#64748b">{pct}%</span>
            </div>
            """, unsafe_allow_html=True)
            st.progress(pct / 100)

    st.markdown("---")
    st.markdown("### 🎯 비전 & 목표")
    st.info("""
    **전력계통 + AI의 융합으로 더 안전하고 스마트한 전력 인프라 구축**

    전기 분야의 깊은 도메인 지식과 데이터 과학, AI 기술을 결합하여
    전력계통 고장 예방 및 운영 최적화 시스템을 개발하는 것을 목표로 합니다.
    나아가 지능형 전력망(스마트 그리드) 시대를 이끌어갈 엔지니어로 성장하겠습니다.
    """)


# ─── CAREER & CERTS ──────────────────────────────────────────────────────────
elif "경력" in page:
    st.markdown("## 📋 경력 & 자격증")
    st.markdown("---")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 📅 경력 사항")
        st.markdown("""
        <div class="timeline-container">
            <div style="margin-bottom:1.5rem;">
                <p style="font-size:1.1rem; font-weight:700; color:#1e3a8a; margin:0;">한전KDN</p>
                <p style="color:#3b82f6; font-weight:600; margin:0.2rem 0;">
                    2022.06 ~ 현재
                    <span style="background:#dbeafe; color:#1e40af; padding:0.1rem 0.5rem;
                                 border-radius:9999px; font-size:0.75rem; margin-left:0.5rem;">재직 중</span>
                </p>
                <p style="color:#64748b; font-size:0.9rem; margin:0.2rem 0;">계통제어부 · 전기직렬</p>
                <ul style="margin-top:0.5rem; color:#374151; line-height:1.8;">
                    <li>SPS 고장파급방지시스템 개발 · 운영</li>
                    <li>변전소 조작지원시스템 구축</li>
                    <li>다기능 정보전송장치 사업 수행</li>
                    <li>AI 기반 전력계통 분석 연구</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        col_a.metric("총 경력", "4년 이상", "2022.06 ~ 현재")
        col_b.metric("소속 부서", "계통제어부", "전기직렬")

    with col2:
        st.markdown("### 📜 보유 자격증")
        st.markdown("""
        <div class="cert-box">
            <p class="cert-name">⚡ 전기기사</p>
            <p class="cert-info">국가기술자격 · 한국산업인력공단</p>
        </div>
        <div class="cert-box">
            <p class="cert-name">🔌 전기공사기사</p>
            <p class="cert-info">국가기술자격 · 한국산업인력공단</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📚 학습 중인 기술")
        for tech, desc in [
            ("Python", "🐍 데이터 분석 & AI 개발"),
            ("Streamlit", "🌊 데이터 시각화 웹앱"),
            ("머신러닝", "🤖 전력계통 이상 감지"),
            ("딥러닝", "🧠 시계열 예측 & 패턴 인식"),
        ]:
            st.markdown(f"- **{tech}**: {desc}")


# ─── PROJECTS ────────────────────────────────────────────────────────────────
elif "프로젝트" in page:
    st.markdown("## 🔧 수행 프로젝트")
    st.markdown("---")

    projects = [
        {
            "icon": "🛡️",
            "title": "SPS 고장파급방지시스템",
            "color": "#dc2626",
            "period": "한전KDN 재직 중 수행",
            "desc": "전력계통의 대규모 정전을 방지하기 위한 System Protection Scheme(SPS) 개발 및 구축 사업. "
                    "실시간 계통 감시를 통해 고장 발생 시 자동으로 대응하는 보호 시스템을 구현하였습니다.",
            "tags": ["전력계통", "보호시스템", "실시간 감시", "IEC 61850", "자동화"],
            "details": [
                "실시간 전력계통 데이터 수집 및 분석 시스템 구축",
                "고장 파급 방지 알고리즘 설계 및 구현",
                "IEC 61850 기반 변전소 통신 프로토콜 적용",
                "고장 이벤트 발생 시 밀리초 단위 자동 대응",
                "24/7 무중단 운영 시스템 설계 및 구축",
            ],
        },
        {
            "icon": "🏭",
            "title": "변전소 조작지원시스템",
            "color": "#2563eb",
            "period": "한전KDN 재직 중 수행",
            "desc": "변전소 운영 인력의 안전하고 효율적인 조작을 지원하는 시스템 구축 사업. "
                    "조작 순서 가이드, 연동 제어, 오조작 방지 기능 등을 구현하여 운전 효율성과 안전성을 향상시켰습니다.",
            "tags": ["변전소", "HMI", "SCADA", "조작지원", "안전"],
            "details": [
                "조작 인터락 및 시퀀스 자동화 구현",
                "운전원 인터페이스(HMI) 설계 및 개선",
                "SCADA 연계 실시간 모니터링 시스템 구축",
                "오조작 방지 다중 확인 시스템 구현",
                "운전 이력 기록 및 분석 기능 개발",
            ],
        },
        {
            "icon": "📡",
            "title": "다기능 정보전송장치",
            "color": "#16a34a",
            "period": "한전KDN 재직 중 수행",
            "desc": "전력계통 각 지점의 정보를 수집하여 중앙 시스템으로 전송하는 다기능 RTU 개발 사업. "
                    "다양한 통신 프로토콜을 지원하는 범용 정보전송 플랫폼을 구축하여 계통 감시 효율을 향상시켰습니다.",
            "tags": ["RTU", "통신", "IEC 60870", "DNP3", "데이터 수집"],
            "details": [
                "다중 통신 프로토콜 지원 (IEC 60870-5, DNP3, IEC 61850)",
                "원격 진단 및 유지보수 기능 구현",
                "고신뢰성 이중화 데이터 전송 아키텍처 설계",
                "전력계통 각 변전소 데이터 통합 수집",
                "실시간 통신 상태 모니터링 및 알람 시스템",
            ],
        },
    ]

    for proj in projects:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])
        st.markdown(f"""
        <div class="project-card" style="border-left-color:{proj['color']};">
            <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:0.75rem;">
                <span style="font-size:2rem;">{proj['icon']}</span>
                <div>
                    <h3 class="project-title" style="color:{proj['color']};">{proj['title']}</h3>
                    <span style="font-size:0.8rem; color:#94a3b8;">{proj['period']}</span>
                </div>
            </div>
            <p class="project-desc">{proj['desc']}</p>
            <div>{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("📋 상세 내용 보기"):
            for detail in proj["details"]:
                st.markdown(f"✅ {detail}")

    st.info("📌 위 프로젝트들은 한전KDN 계통제어부에서 수행한 전력계통 핵심 사업들입니다.")
