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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700;1,900&family=Noto+Serif+KR:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;500;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --bg:       #f7f3ec;
    --surface:  #ffffff;
    --primary:  #1a1032;
    --accent:   #c9a84c;
    --accent-p: #f0e6c8;
    --text:     #2a2245;
    --muted:    #7e7899;
    --border:   #e5e0d8;
    --sidebar:  #120d26;
}

/* ── base ── */
[data-testid="stApp"]          { background: var(--bg) !important; }
[data-testid="stSidebar"]      { background: var(--sidebar) !important; }
[data-testid="stSidebar"] > div:first-child { background: var(--sidebar) !important; }

.block-container { padding: 2.5rem 3rem !important; max-width: 1150px; }
#MainMenu, footer, header { visibility: hidden; }

/* ── display typography ── */
.d-name {
    font-family: 'Playfair Display', 'Noto Serif KR', Georgia, serif;
    font-size: 5rem; font-weight: 900; font-style: italic;
    color: var(--primary); line-height: 1.0;
    letter-spacing: -0.03em; margin: 0;
}
.d-role {
    font-family: 'Noto Sans KR', 'DM Sans', sans-serif;
    font-size: 0.78rem; color: var(--muted);
    letter-spacing: 0.22em; text-transform: uppercase;
    margin: 1rem 0 0; font-weight: 400;
}
.d-body {
    font-family: 'Noto Sans KR', 'DM Sans', sans-serif;
    font-size: 0.95rem; color: var(--text);
    line-height: 1.95; font-weight: 300;
}
.sec-label {
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.68rem; color: var(--accent);
    letter-spacing: 0.3em; text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.sec-title {
    font-family: 'Playfair Display', 'Noto Serif KR', Georgia, serif;
    font-size: 2rem; font-weight: 700; color: var(--primary);
    margin: 0 0 0.5rem; line-height: 1.2;
}

/* ── gold divider ── */
.g-line {
    height: 1px;
    background: linear-gradient(90deg, var(--accent) 0%, transparent 65%);
    border: none; margin: 2rem 0;
}

/* ── stat blocks ── */
.stat-wrap { border-top: 1px solid var(--accent); padding-top: 1.25rem; }
.stat-n {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 3.2rem; font-weight: 700; font-style: italic;
    color: var(--primary); line-height: 1; margin: 0;
}
.stat-l {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.68rem; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.15em; margin-top: 0.4rem;
}

/* ── interest tags ── */
.i-tag {
    display: inline-block;
    border: 1px solid rgba(42,34,69,0.25);
    color: var(--text); padding: 0.42rem 1.1rem;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.82rem; margin: 0.3rem 0.2rem;
    letter-spacing: 0.04em; background: transparent;
}

/* ── project cards ── */
.p-card {
    display: flex; background: var(--surface);
    margin-bottom: 2.25rem;
    box-shadow: 0 2px 28px rgba(26,16,50,0.07);
    position: relative; overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.p-bar { width: 5px; flex-shrink: 0; }
.p-body { padding: 2rem 5rem 2rem 2.25rem; flex: 1; }
.p-num {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 5.5rem; font-weight: 900; font-style: italic;
    color: var(--accent-p); line-height: 1;
    position: absolute; right: 1.75rem; top: 1.25rem;
    user-select: none; pointer-events: none;
}
.p-title {
    font-family: 'Noto Serif KR', Georgia, serif;
    font-size: 1.2rem; font-weight: 700;
    color: var(--primary); margin: 0 0 0.6rem;
    letter-spacing: -0.01em;
}
.p-period {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem; color: var(--muted);
    letter-spacing: 0.1em; text-transform: uppercase;
    margin-bottom: 0.75rem;
}
.p-desc {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.875rem; color: var(--muted);
    line-height: 1.85; margin-bottom: 1.1rem; font-weight: 300;
}
.p-tag {
    display: inline-block;
    border: 1px solid var(--border); color: var(--muted);
    padding: 0.14rem 0.62rem;
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase;
    margin: 0.15rem 0.1rem;
}

/* ── cert card ── */
.c-card {
    border-left: 2px solid var(--accent);
    padding: 1.1rem 1.6rem;
    background: var(--surface); margin-bottom: 1rem;
    box-shadow: 0 1px 8px rgba(26,16,50,0.04);
}
.c-name {
    font-family: 'Noto Serif KR', Georgia, serif;
    font-size: 1rem; font-weight: 700;
    color: var(--primary); margin: 0 0 0.25rem;
}
.c-sub {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.78rem; color: var(--muted); margin: 0;
}

/* ── skill bar (custom HTML) ── */
.sk-row { margin-bottom: 1.35rem; }
.sk-head {
    font-family: 'Noto Serif KR', Georgia, serif;
    font-size: 0.88rem; color: var(--text);
    display: flex; justify-content: space-between; margin-bottom: 0.4rem;
}
.sk-pct {
    font-family: 'Playfair Display', Georgia, serif;
    font-style: italic; font-size: 0.82rem; color: var(--accent);
}
.sk-track {
    height: 2px; background: var(--border); position: relative;
}
.sk-fill {
    height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent));
    position: absolute; top: 0; left: 0;
}

/* ── timeline ── */
.tl { position: relative; padding-left: 2.25rem; }
.tl::before {
    content: ''; position: absolute; left: 6px; top: 10px; bottom: 0;
    width: 1px;
    background: linear-gradient(to bottom, var(--accent) 0%, transparent 85%);
}
.tl-dot {
    position: absolute; left: 0; top: 10px;
    width: 12px; height: 12px;
    background: var(--accent); border-radius: 50%;
    border: 3px solid var(--bg);
    box-shadow: 0 0 0 1px var(--accent);
}
.tl-co {
    font-family: 'Noto Serif KR', Georgia, serif;
    font-size: 1.2rem; font-weight: 700;
    color: var(--primary); margin: 0;
}
.tl-period {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem; color: var(--accent);
    letter-spacing: 0.06em; margin: 0.25rem 0;
}
.tl-dept {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.8rem; color: var(--muted); margin: 0 0 0.9rem;
}
.tl-li {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.85rem; color: var(--text); line-height: 1.75;
    font-weight: 300; padding: 0.35rem 0 0.35rem 0.9rem;
    border-left: 1px solid var(--border); margin-bottom: 0.3rem;
}

/* ── info table ── */
.info-row {
    display: flex; border-bottom: 1px solid var(--border);
    padding: 0.75rem 0; align-items: baseline;
}
.info-k {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.7rem; font-weight: 500; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.12em; width: 82px; flex-shrink: 0;
}
.info-v {
    font-family: 'Noto Serif KR', Georgia, serif;
    font-size: 0.92rem; color: var(--text);
}

/* ── vision block ── */
.vision-box {
    border: 1px solid var(--border); padding: 2rem 2.25rem;
    background: var(--surface);
    border-left: 3px solid var(--accent);
    box-shadow: 0 2px 20px rgba(26,16,50,0.05);
}
.vision-q {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.5rem; font-style: italic; color: var(--accent);
    margin: 0 0 1rem; line-height: 1.4;
}
.vision-p {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.9rem; color: var(--text); line-height: 1.9; font-weight: 300;
}

/* ── sidebar nav ── */
[data-testid="stSidebar"] label {
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #a09ab4 !important;
}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"] {
    margin-bottom: 0.25rem;
}
[data-testid="stSidebar"] p { color: #c0b8d0 !important; }
[data-testid="stSidebar"] .stFileUploader {
    background: rgba(255,255,255,0.04) !important;
    border: 1px dashed rgba(255,255,255,0.15) !important;
    border-radius: 2px !important;
}
[data-testid="stSidebar"] .stFileUploader label { color: #7a7090 !important; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.08) !important; }
</style>
""", unsafe_allow_html=True)

# ── session ──────────────────────────────────────────────────────────────────
if "profile_img" not in st.session_state:
    st.session_state.profile_img = None

# ── sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.5rem 0 1rem;">
        <p style="font-family:'Playfair Display',Georgia,serif;
                  font-size:1.55rem; font-weight:900; font-style:italic;
                  color:#f0ece4; margin:0; letter-spacing:-0.01em;">
            Lim Won-seop
        </p>
        <p style="font-family:'Noto Sans KR',sans-serif;
                  font-size:0.68rem; color:#6a608a;
                  letter-spacing:0.2em; text-transform:uppercase; margin:0.4rem 0 0;">
            Engineer · 한전KDN
        </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "프로필 사진",
        type=["jpg", "jpeg", "png"],
        label_visibility="visible"
    )
    if uploaded:
        img = Image.open(uploaded)
        w, h = img.size
        s = min(w, h)
        img = img.crop(((w-s)//2, (h-s)//2, (w+s)//2, (h+s)//2)).resize((240, 240))
        st.session_state.profile_img = img

    if st.session_state.profile_img:
        st.image(st.session_state.profile_img, use_container_width=True)
    else:
        st.markdown("""
        <div style="width:100%; aspect-ratio:1/1; background:#1e1640;
                    display:flex; align-items:center; justify-content:center;
                    font-size:4.5rem; border:1px solid #2e2655;">
            ⚡
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["홈", "소개", "경력 & 자격증", "프로젝트"],
        label_visibility="collapsed"
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Noto Sans KR',sans-serif; font-size:0.72rem;
                color:#5a5272; line-height:2.2; padding-bottom:1rem;">
        wonseob_123@kdn.com<br>
        계통제어부
    </div>
    """, unsafe_allow_html=True)


# ── HOME ─────────────────────────────────────────────────────────────────────
if page == "홈":

    col1, col2 = st.columns([11, 7], gap="large")

    with col1:
        st.markdown('<p class="sec-label">포트폴리오</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="d-name">임원섭</h1>', unsafe_allow_html=True)
        st.markdown('<p class="d-role">Power Systems Engineer · AI & Data · 한전KDN 계통제어부</p>',
                    unsafe_allow_html=True)
        st.markdown('<hr class="g-line">', unsafe_allow_html=True)
        st.markdown("""
        <p class="d-body">
        전력 계통의 안정적인 운영과 미래 기술을 연구하는 전기직렬 엔지니어입니다.<br>
        SPS 고장파급방지시스템, 변전소 자동화, 다기능 정보전송장치 분야의
        핵심 사업들을 수행하였으며,<br>현재는 <strong>AI · 데이터 기술</strong>과
        전력계통의 융합 연구에 집중하고 있습니다.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div>
            <span class="i-tag">전력계통</span>
            <span class="i-tag">AI · 머신러닝</span>
            <span class="i-tag">데이터 분석</span>
            <span class="i-tag">변전소 자동화</span>
            <span class="i-tag">고장파급방지</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.session_state.profile_img:
            st.image(st.session_state.profile_img.resize((320, 320)), use_container_width=True)
        else:
            st.markdown("""
            <div style="width:100%; aspect-ratio:1/1; background:#1a1032;
                        display:flex; align-items:center; justify-content:center;
                        font-size:7rem; border:1px solid #2e2655;">
                ⚡
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (n, l) in zip([c1,c2,c3,c4],
                           [("3+","수행 프로젝트"),("2","보유 자격증"),
                            ("4+","경력 (년)"),("∞","성장 의지")]):
        with col:
            st.markdown(f"""
            <div class="stat-wrap">
                <p class="stat-n">{n}</p>
                <p class="stat-l">{l}</p>
            </div>
            """, unsafe_allow_html=True)


# ── ABOUT ────────────────────────────────────────────────────────────────────
elif page == "소개":

    st.markdown('<p class="sec-label">About</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">소개</h2>', unsafe_allow_html=True)
    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="sec-label" style="margin-bottom:1.2rem;">기본 정보</p>',
                    unsafe_allow_html=True)
        for k, v in [("이름","임원섭"),("소속","한전KDN"),("부서","계통제어부"),
                     ("직렬","전기직렬"),("관심","AI, 데이터, 전력계통"),
                     ("이메일","wonseob_123@kdn.com")]:
            st.markdown(f"""
            <div class="info-row">
                <span class="info-k">{k}</span>
                <span class="info-v">{v}</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="sec-label" style="margin-bottom:1.2rem;">기술 역량</p>',
                    unsafe_allow_html=True)
        for skill, pct in [("전력계통 분석",90),("변전소 시스템",85),
                           ("데이터 분석",75),("AI · 머신러닝",70),
                           ("파이썬 프로그래밍",68)]:
            st.markdown(f"""
            <div class="sk-row">
                <div class="sk-head">
                    <span>{skill}</span>
                    <span class="sk-pct">{pct}</span>
                </div>
                <div class="sk-track">
                    <div class="sk-fill" style="width:{pct}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="g-line">', unsafe_allow_html=True)
    st.markdown('<p class="sec-label">Vision</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="vision-box">
        <p class="vision-q">"전력계통과 AI의 융합으로<br>더 안전한 인프라를."</p>
        <p class="vision-p">
        전기 분야의 깊은 도메인 지식과 데이터 과학, AI 기술을 결합하여
        전력계통 고장 예방 및 운영 최적화 시스템 개발을 목표로 합니다.<br><br>
        나아가 지능형 전력망(스마트 그리드) 시대를 이끌어갈 엔지니어로 성장하겠습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ── CAREER & CERTS ───────────────────────────────────────────────────────────
elif page == "경력 & 자격증":

    st.markdown('<p class="sec-label">Career &amp; Certifications</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">경력 & 자격증</h2>', unsafe_allow_html=True)
    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="sec-label" style="margin-bottom:1.5rem;">경력 사항</p>',
                    unsafe_allow_html=True)
        st.markdown("""
        <div class="tl">
            <div class="tl-dot"></div>
            <p class="tl-co">한전KDN</p>
            <p class="tl-period">2022.06 — 현재 &nbsp;·&nbsp; 재직 중</p>
            <p class="tl-dept">계통제어부 · 전기직렬</p>
            <div class="tl-li">SPS 고장파급방지시스템 개발 · 운영</div>
            <div class="tl-li">변전소 조작지원시스템 구축</div>
            <div class="tl-li">다기능 정보전송장치 사업 수행</div>
            <div class="tl-li">AI 기반 전력계통 분석 연구</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        ca, cb = st.columns(2)
        for col, (n, l) in zip([ca, cb],
                               [("4년+","총 경력"),("전기직렬","직렬")]):
            with col:
                st.markdown(f"""
                <div class="stat-wrap">
                    <p class="stat-n" style="font-size:2rem;">{n}</p>
                    <p class="stat-l">{l}</p>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="sec-label" style="margin-bottom:1.5rem;">보유 자격증</p>',
                    unsafe_allow_html=True)
        for name, sub in [
            ("전기기사", "국가기술자격 · 한국산업인력공단"),
            ("전기공사기사", "국가기술자격 · 한국산업인력공단"),
        ]:
            st.markdown(f"""
            <div class="c-card">
                <p class="c-name">{name}</p>
                <p class="c-sub">{sub}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<br><p class="sec-label" style="margin-bottom:1rem;">학습 중인 기술</p>',
                    unsafe_allow_html=True)
        for tech, desc in [("Python","데이터 분석 & AI 개발"),
                           ("Streamlit","데이터 시각화 웹앱"),
                           ("머신러닝","전력계통 이상 감지"),
                           ("딥러닝","시계열 예측 & 패턴 인식")]:
            st.markdown(f"""
            <div class="info-row">
                <span class="info-k">{tech}</span>
                <span class="info-v" style="font-size:0.85rem; font-family:'Noto Sans KR',sans-serif;
                      color:var(--muted); font-weight:300;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)


# ── PROJECTS ─────────────────────────────────────────────────────────────────
elif page == "프로젝트":

    st.markdown('<p class="sec-label">Selected Works</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">수행 프로젝트</h2>', unsafe_allow_html=True)
    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    projects = [
        {
            "num": "01",
            "title": "SPS 고장파급방지시스템",
            "color": "#b5342a",
            "period": "KDN · 계통제어부",
            "desc": "전력계통의 대규모 정전을 방지하기 위한 System Protection Scheme(SPS) 개발 및 구축 사업. "
                    "실시간 계통 감시를 통해 고장 발생 시 밀리초 단위로 자동 대응하는 보호 시스템을 구현하였습니다.",
            "tags": ["전력계통","보호시스템","IEC 61850","실시간 감시","자동화"],
            "details": [
                "실시간 전력계통 데이터 수집 및 분석 시스템 구축",
                "고장 파급 방지 알고리즘 설계 및 구현",
                "IEC 61850 기반 변전소 통신 프로토콜 적용",
                "고장 이벤트 발생 시 밀리초 단위 자동 대응",
                "24/7 무중단 운영 시스템 설계 및 구축",
            ],
        },
        {
            "num": "02",
            "title": "변전소 조작지원시스템",
            "color": "#1e4fad",
            "period": "KDN · 계통제어부",
            "desc": "변전소 운영 인력의 안전하고 효율적인 조작을 지원하는 시스템 구축 사업. "
                    "조작 순서 가이드, 인터락, 오조작 방지 기능을 구현하여 운전 효율성과 안전성을 크게 향상시켰습니다.",
            "tags": ["변전소","HMI","SCADA","조작지원","안전"],
            "details": [
                "조작 인터락 및 시퀀스 자동화 구현",
                "운전원 인터페이스(HMI) 설계 및 개선",
                "SCADA 연계 실시간 모니터링 시스템 구축",
                "오조작 방지 다중 확인 시스템 구현",
                "운전 이력 기록 및 분석 기능 개발",
            ],
        },
        {
            "num": "03",
            "title": "다기능 정보전송장치",
            "color": "#1a7a4a",
            "period": "KDN · 계통제어부",
            "desc": "전력계통 각 지점의 정보를 수집하여 중앙 시스템으로 전송하는 다기능 RTU 개발 사업. "
                    "다중 통신 프로토콜을 지원하는 범용 플랫폼을 구축하여 계통 감시 효율을 향상시켰습니다.",
            "tags": ["RTU","IEC 60870","DNP3","데이터 수집","이중화"],
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
        tags_html = "".join(f'<span class="p-tag">{t}</span>' for t in proj["tags"])
        st.markdown(f"""
        <div class="p-card">
            <div class="p-bar" style="background:{proj['color']};"></div>
            <div class="p-body">
                <p class="p-period">{proj['period']}</p>
                <p class="p-title">{proj['title']}</p>
                <p class="p-desc">{proj['desc']}</p>
                <div>{tags_html}</div>
            </div>
            <div class="p-num">{proj['num']}</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("상세 내용 보기"):
            for detail in proj["details"]:
                st.markdown(
                    f'<p style="font-family:\'Noto Sans KR\',sans-serif; font-size:0.88rem;'
                    f'color:#2a2245; line-height:1.7; font-weight:300; margin:0.4rem 0;">'
                    f'— {detail}</p>',
                    unsafe_allow_html=True
                )

    st.markdown("""
    <p style="font-family:'Noto Sans KR',sans-serif; font-size:0.78rem; color:#7e7899;
              text-align:center; letter-spacing:0.1em; margin-top:1rem;">
    한전KDN 계통제어부 수행 전력계통 핵심 사업
    </p>
    """, unsafe_allow_html=True)
