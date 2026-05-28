import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="임원섭 | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Black+Han+Sans&family=Noto+Sans+KR:wght@300;400;700;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap');

:root {
    --bg:      #f5f1ea;
    --s1:      #ffffff;
    --s2:      #ede9e2;
    --accent:  #d42e2e;
    --gold:    #b8922e;
    --text:    #0f0e18;
    --muted:   #7a7688;
    --dim:     #ccc8bf;
    --border:  #e3dfd7;
    --sb:      #0f0f1a;
}

/* ── base ── */
[data-testid="stApp"]                      { background: var(--bg) !important; }
[data-testid="stSidebar"]                  { background: var(--sb) !important; }
[data-testid="stSidebar"] > div:first-child{ background: var(--sb) !important; }
.block-container { padding: 2.5rem 3rem !important; max-width: 1200px; }
#MainMenu, footer, header { visibility: hidden; }

/* subtle grain overlay */
[data-testid="stApp"]::before {
    content: '';
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background-image:
        linear-gradient(rgba(0,0,0,0.012) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,0,0,0.012) 1px, transparent 1px);
    background-size: 48px 48px;
}

/* ── hero typography ── */
.hero-eyebrow {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.8rem; color: var(--accent);
    letter-spacing: 0.38em; margin: 0 0 0.6rem;
}
.hero-name {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 7rem; font-weight: 900;
    color: var(--text); line-height: 0.88;
    letter-spacing: -0.02em; margin: 0;
}
.hero-name-en {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.9rem; color: var(--muted);
    letter-spacing: 0.2em; margin: 0.6rem 0 0;
}
.hero-rule {
    width: 52px; height: 3px;
    background: var(--accent);
    border: none; margin: 1.5rem 0;
}
.hero-body {
    font-family: 'Noto Sans KR', 'DM Sans', sans-serif;
    font-size: 0.9rem; color: var(--muted);
    line-height: 1.95; font-weight: 300; max-width: 480px;
}

/* ── interest tags ── */
.i-tag {
    display: inline-block;
    border: 1px solid var(--dim); color: var(--muted);
    padding: 0.3rem 0.85rem;
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.72rem; margin: 0.25rem 0.15rem;
    letter-spacing: 0.08em; text-transform: uppercase;
}

/* ── stat blocks ── */
.stat-block { border-top: 1px solid var(--dim); padding-top: 1.3rem; }
.stat-n {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4.2rem; color: var(--text);
    line-height: 1; margin: 0; letter-spacing: 0.03em;
}
.stat-n.red  { color: var(--accent); }
.stat-n.gold { color: var(--gold); }
.stat-l {
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.66rem; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.2em; margin-top: 0.35rem;
}

/* ── section headers ── */
.sec-label {
    font-family: 'Bebas Neue', 'DM Sans', sans-serif;
    font-size: 0.72rem; color: var(--accent);
    letter-spacing: 0.38em; text-transform: uppercase; margin-bottom: 0.5rem;
}
.sec-title {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 2.6rem; color: var(--text);
    margin: 0 0 0.25rem; line-height: 1.1;
}
.g-line { height: 1px; background: var(--border); border: none; margin: 2rem 0; }

/* ── project cards ── */
.p-card {
    background: var(--s1); border: 1px solid var(--border);
    border-top: none; position: relative; overflow: hidden;
    margin-bottom: 1.5rem;
}
.p-topbar { height: 3px; width: 100%; position: absolute; top: 0; left: 0; }
.p-body   { padding: 2rem 7rem 1.75rem 2.5rem; }
.p-bgnum {
    font-family: 'Bebas Neue', sans-serif; font-size: 9rem;
    line-height: 1; position: absolute; right: 1.5rem; top: 0.25rem;
    color: var(--border); user-select: none; pointer-events: none;
    letter-spacing: 0.02em; opacity: 1;
}
.p-period {
    font-family: 'Bebas Neue', 'DM Sans', sans-serif;
    font-size: 0.7rem; color: var(--muted);
    letter-spacing: 0.22em; text-transform: uppercase; margin-bottom: 0.45rem;
}
.p-title {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 1.3rem; color: var(--text); margin: 0 0 0.75rem;
}
.p-desc {
    font-family: 'Noto Sans KR', 'DM Sans', sans-serif;
    font-size: 0.875rem; color: var(--muted);
    line-height: 1.9; margin-bottom: 1.1rem; font-weight: 300;
}
.p-tag {
    display: inline-block; border: 1px solid var(--dim); color: var(--muted);
    padding: 0.12rem 0.58rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.64rem; letter-spacing: 0.14em; text-transform: uppercase;
    margin: 0.12rem 0.08rem;
}

/* ── info rows ── */
.info-row {
    display: flex; border-bottom: 1px solid var(--border);
    padding: 0.78rem 0; align-items: baseline;
}
.info-k {
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.66rem; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.15em;
    width: 82px; flex-shrink: 0;
}
.info-v {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.9rem; color: var(--text); font-weight: 400;
}

/* ── skill bars ── */
.sk-row { margin-bottom: 1.4rem; }
.sk-head {
    font-family: 'Noto Sans KR', sans-serif; font-size: 0.85rem;
    color: var(--text); display: flex; justify-content: space-between;
    margin-bottom: 0.5rem;
}
.sk-pct {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.92rem; color: var(--accent); letter-spacing: 0.06em;
}
.sk-track { height: 2px; background: var(--dim); position: relative; }
.sk-fill  { height: 100%; background: var(--accent); position: absolute; top: 0; left: 0; }

/* ── cert cards ── */
.c-card {
    background: var(--s1); border: 1px solid var(--border);
    border-left: 2px solid var(--gold);
    padding: 1.25rem 1.6rem; margin-bottom: 0.85rem;
}
.c-name {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 1rem; color: var(--text); margin: 0 0 0.25rem;
}
.c-sub {
    font-family: 'DM Sans', sans-serif; font-size: 0.72rem;
    color: var(--muted); letter-spacing: 0.08em; margin: 0;
}

/* ── timeline ── */
.tl { position: relative; padding-left: 2.25rem; }
.tl::before {
    content: ''; position: absolute; left: 6px; top: 12px; bottom: 0;
    width: 1px;
    background: linear-gradient(to bottom, var(--accent) 0%, transparent 80%);
}
.tl-dot {
    position: absolute; left: 0; top: 12px;
    width: 12px; height: 12px;
    background: var(--accent); border-radius: 50%;
    border: 3px solid var(--bg);
    box-shadow: 0 0 0 1px var(--accent);
}
.tl-co {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 1.3rem; color: var(--text); margin: 0;
}
.tl-period {
    font-family: 'Bebas Neue', 'DM Sans', sans-serif;
    font-size: 0.85rem; color: var(--accent);
    letter-spacing: 0.1em; margin: 0.3rem 0 0.15rem;
}
.tl-dept {
    font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    font-size: 0.72rem; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.12em; margin: 0 0 1rem;
}
.tl-li {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.85rem; color: var(--muted);
    line-height: 1.75; font-weight: 300;
    padding: 0.35rem 0 0.35rem 0.9rem;
    border-left: 1px solid var(--border); margin-bottom: 0.3rem;
}

/* ── vision ── */
.vision-box {
    background: var(--s1); border: 1px solid var(--border);
    border-top: 2px solid var(--accent); padding: 2rem 2.5rem;
}
.vision-headline {
    font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;
    font-size: 1.4rem; color: var(--text);
    line-height: 1.55; margin: 0 0 1rem;
}
.vision-body {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.88rem; color: var(--muted);
    line-height: 1.95; font-weight: 300;
}

/* ── expander (dark) ── */
[data-testid="stExpander"] {
    background: var(--s1) !important;
    border: 1px solid var(--border) !important;
    border-radius: 0 !important;
}
[data-testid="stExpander"] summary {
    font-family: 'Bebas Neue', 'DM Sans', sans-serif !important;
    font-size: 0.8rem !important; letter-spacing: 0.2em !important;
    color: var(--muted) !important;
}

/* ── sidebar ── */
[data-testid="stSidebar"] label {
    font-family: 'Bebas Neue', 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important; letter-spacing: 0.22em !important;
    color: #5a5870 !important;
}
[data-testid="stSidebar"] p    { color: #5a5870 !important; }
[data-testid="stSidebar"] hr   { border-color: #1e1e30 !important; }
[data-testid="stSidebar"] .stFileUploader {
    background: rgba(255,255,255,0.03) !important;
    border: 1px dashed #2a2a42 !important; border-radius: 0 !important;
}
[data-testid="stSidebar"] .stFileUploader label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.72rem !important; color: #4a4a62 !important;
}
</style>
""", unsafe_allow_html=True)

# ── session ──────────────────────────────────────────────────────────────────
if "profile_img" not in st.session_state:
    st.session_state.profile_img = None

# ── sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.75rem 0 1rem;">
        <p style="font-family:'Bebas Neue',sans-serif; font-size:1.6rem;
                  color:#edecf2; margin:0; letter-spacing:0.12em;">
            LIM WON-SEOP
        </p>
        <p style="font-family:'DM Sans',sans-serif; font-size:0.65rem;
                  color:#3a3a55; letter-spacing:0.28em; text-transform:uppercase;
                  margin:0.35rem 0 0;">
            Engineer · 한전KDN
        </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("프로필 사진", type=["jpg","jpeg","png"],
                                 label_visibility="visible")
    if uploaded:
        img = Image.open(uploaded)
        w, h = img.size; s = min(w, h)
        img = img.crop(((w-s)//2,(h-s)//2,(w+s)//2,(h+s)//2)).resize((240,240))
        st.session_state.profile_img = img

    if st.session_state.profile_img:
        st.image(st.session_state.profile_img, use_container_width=True)
    else:
        st.markdown("""
        <div style="width:100%; aspect-ratio:1/1; background:#0e0e1a;
                    display:flex; align-items:center; justify-content:center;
                    font-size:4.5rem; border:1px solid #1a1a2e;">
            ⚡
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    page = st.radio("nav",
                    ["홈", "소개", "경력 & 자격증", "프로젝트"],
                    label_visibility="collapsed")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'DM Sans',sans-serif; font-size:0.68rem;
                color:#2e2e45; line-height:2.4; padding-bottom:1rem;
                letter-spacing:0.06em;">
        wonseob_123@kdn.com<br>
        계통제어부
    </div>
    """, unsafe_allow_html=True)


# ── HOME ─────────────────────────────────────────────────────────────────────
if page == "홈":

    col1, col2 = st.columns([11, 7], gap="large")

    with col1:
        st.markdown('<p class="hero-eyebrow">Power Systems Engineer · AI · Data</p>',
                    unsafe_allow_html=True)
        st.markdown('<h1 class="hero-name">임원섭</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-name-en">LIM WON-SEOP</p>', unsafe_allow_html=True)
        st.markdown('<hr class="hero-rule">', unsafe_allow_html=True)
        st.markdown("""
        <p class="hero-body">
        전력 계통의 안정적인 운영과 미래 기술을 연구하는 전기직렬 엔지니어.<br>
        SPS 고장파급방지, 변전소 자동화, 정보전송장치 분야의 핵심 사업들을 수행하였으며<br>
        현재는 AI · 데이터 기술과 전력계통의 융합에 집중하고 있다.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div>
            <span class="i-tag">전력계통</span>
            <span class="i-tag">AI · ML</span>
            <span class="i-tag">데이터</span>
            <span class="i-tag">변전소</span>
            <span class="i-tag">고장파급방지</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.session_state.profile_img:
            st.image(st.session_state.profile_img.resize((320, 320)), use_container_width=True)
        else:
            st.markdown("""
            <div style="width:100%; aspect-ratio:1/1; background:#0f0f1c;
                        display:flex; align-items:center; justify-content:center;
                        border:1px solid #1e1e35; font-size:7rem;">
                ⚡
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (n, l, cls) in zip(
        [c1, c2, c3, c4],
        [("4+","경력 (년)","red"), ("3+","수행 프로젝트",""), ("2","보유 자격증","gold"), ("∞","성장 의지","")]
    ):
        with col:
            st.markdown(f"""
            <div class="stat-block">
                <p class="stat-n {cls}">{n}</p>
                <p class="stat-l">{l}</p>
            </div>
            """, unsafe_allow_html=True)


# ── ABOUT ────────────────────────────────────────────────────────────────────
elif page == "소개":

    st.markdown('<p class="sec-label">About</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">소개</h2>', unsafe_allow_html=True)
    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<p class="sec-label" style="margin-bottom:1.25rem;">기본 정보</p>',
                    unsafe_allow_html=True)
        for k, v in [("이름","임원섭"), ("소속","한전KDN"), ("부서","계통제어부"),
                     ("직렬","전기직렬"), ("관심","AI · 데이터 · 전력계통"),
                     ("이메일","wonseob_123@kdn.com")]:
            st.markdown(f"""
            <div class="info-row">
                <span class="info-k">{k}</span>
                <span class="info-v">{v}</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="sec-label" style="margin-bottom:1.25rem;">기술 역량</p>',
                    unsafe_allow_html=True)
        for skill, pct in [("전력계통 분석",90), ("변전소 시스템",85),
                           ("데이터 분석",75), ("AI · 머신러닝",70),
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
        <p class="vision-headline">전력계통과 AI의 융합으로<br>더 안전한 전력 인프라를 만든다.</p>
        <p class="vision-body">
        전기 분야의 깊은 도메인 지식과 데이터 과학, AI 기술을 결합하여
        전력계통 고장 예방 및 운영 최적화 시스템 개발을 목표로 합니다.<br><br>
        지능형 전력망(스마트 그리드) 시대를 이끌어갈 엔지니어로 성장하겠습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ── CAREER & CERTS ───────────────────────────────────────────────────────────
elif page == "경력 & 자격증":

    st.markdown('<p class="sec-label">Career &amp; Certifications</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sec-title">경력 & 자격증</h2>', unsafe_allow_html=True)
    st.markdown('<hr class="g-line">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<p class="sec-label" style="margin-bottom:1.5rem;">경력 사항</p>',
                    unsafe_allow_html=True)
        st.markdown("""
        <div class="tl">
            <div class="tl-dot"></div>
            <p class="tl-co">한전KDN</p>
            <p class="tl-period">2022.06 — PRESENT</p>
            <p class="tl-dept">계통제어부 · 전기직렬</p>
            <div class="tl-li">SPS 고장파급방지시스템 개발 · 운영</div>
            <div class="tl-li">변전소 조작지원시스템 구축</div>
            <div class="tl-li">다기능 정보전송장치 사업 수행</div>
            <div class="tl-li">AI 기반 전력계통 분석 연구</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        ca, cb = st.columns(2)
        for col, (n, l, c) in zip([ca, cb],
                                   [("4+","총 경력","red"),("전기","직렬","gold")]):
            with col:
                st.markdown(f"""
                <div class="stat-block">
                    <p class="stat-n {c}" style="font-size:2.5rem;">{n}</p>
                    <p class="stat-l">{l}</p>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="sec-label" style="margin-bottom:1.5rem;">보유 자격증</p>',
                    unsafe_allow_html=True)
        for name, sub in [("전기기사","국가기술자격 · 한국산업인력공단"),
                          ("전기공사기사","국가기술자격 · 한국산업인력공단")]:
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
                <span class="info-v" style="font-family:'Noto Sans KR',sans-serif;
                      font-size:0.85rem; color:var(--muted); font-weight:300;">{desc}</span>
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
            "color": "#e03535",
            "period": "KDN · 계통제어부",
            "desc": "전력계통의 대규모 정전을 방지하기 위한 System Protection Scheme(SPS) 개발 및 구축 사업. "
                    "실시간 계통 감시를 통해 고장 발생 시 밀리초 단위로 자동 대응하는 보호 시스템을 구현하였습니다.",
            "tags": ["전력계통","SPS","IEC 61850","실시간 감시","자동화"],
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
            "color": "#2563eb",
            "period": "KDN · 계통제어부",
            "desc": "변전소 운영 인력의 안전하고 효율적인 조작을 지원하는 시스템 구축 사업. "
                    "인터락, 오조작 방지, 조작 시퀀스 가이드 기능을 구현하여 운전 효율성과 안전성을 향상시켰습니다.",
            "tags": ["변전소","HMI","SCADA","인터락","안전"],
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
            "color": "#16a34a",
            "period": "KDN · 계통제어부",
            "desc": "전력계통 각 지점의 정보를 수집하여 중앙 시스템으로 전송하는 다기능 RTU 개발 사업. "
                    "다중 통신 프로토콜을 지원하는 범용 플랫폼으로 계통 감시 효율을 크게 향상시켰습니다.",
            "tags": ["RTU","IEC 60870","DNP3","이중화","데이터 수집"],
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
            <div class="p-topbar" style="background:{proj['color']};"></div>
            <div class="p-body">
                <p class="p-period">{proj['period']}</p>
                <p class="p-title">{proj['title']}</p>
                <p class="p-desc">{proj['desc']}</p>
                <div>{tags_html}</div>
            </div>
            <div class="p-bgnum">{proj['num']}</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("DETAILS"):
            for detail in proj["details"]:
                st.markdown(
                    f'<p style="font-family:\'Noto Sans KR\',sans-serif; font-size:0.875rem;'
                    f'color:#7c7a96; line-height:1.75; font-weight:300; margin:0.4rem 0;">'
                    f'— &nbsp;{detail}</p>',
                    unsafe_allow_html=True
                )

    st.markdown("""
    <p style="font-family:'DM Sans',sans-serif; font-size:0.7rem; color:#38384e;
              text-align:center; letter-spacing:0.2em; text-transform:uppercase; margin-top:1.5rem;">
    한전KDN 계통제어부 수행 전력계통 핵심 사업
    </p>
    """, unsafe_allow_html=True)
