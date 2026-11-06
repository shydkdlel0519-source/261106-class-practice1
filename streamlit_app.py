import html

import streamlit as st

st.set_page_config(page_title="나를 만나는 작은 숲", page_icon="🌿", layout="wide")

story_pages = [
    {
        "chapter": "첫 번째 장",
        "heading": "생일",
        "value": "2007.05.12.",
        "note": "세상에 처음 인사를 건넨 날, 나만의 이야기가 시작되었어요.",
        "image": "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1400&q=85",
        "alt": "햇살이 비치는 초록 들판",
        "caption": "나의 첫 번째 계절",
    },
    {
        "chapter": "두 번째 장",
        "heading": "이름",
        "value": "신하영",
        "note": "나를 부르는 소리에는 나를 아끼는 사람들의 마음이 담겨 있어요.",
        "image": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1400&q=85",
        "alt": "햇빛을 머금은 들꽃",
        "caption": "이름처럼 피어난 꽃",
    },
    {
        "chapter": "세 번째 장",
        "heading": "나이",
        "value": "만 19세",
        "note": "하루하루 자라며 지금의 나를 만들어 가는 중이에요.",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1400&q=85",
        "alt": "잔잔한 호수와 산의 풍경",
        "caption": "자라나는 시간",
    },
    {
        "chapter": "네 번째 장",
        "heading": "소속",
        "value": "청주교육대학교 · 더꿈의교회",
        "note": "함께 걷는 사람들이 있어 나의 숲은 조금 더 넓어져요.",
        "image": "https://images.unsplash.com/photo-1511497584788-876760111969?auto=format&fit=crop&w=1400&q=85",
        "alt": "나무가 빽빽하게 자란 숲길",
        "caption": "함께 걷는 숲길",
    },
    {
        "chapter": "다섯 번째 장",
        "heading": "좋아하는 것",
        "value": "산책 · 뜨개질 · 초콜릿",
        "note": "생각만 해도 마음이 환해지는 것들을 하나씩 모아 보아요.",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1400&q=85",
        "alt": "초록빛이 가득한 숲",
        "caption": "마음이 쉬어 가는 곳",
    },
    {
        "chapter": "여섯 번째 장",
        "heading": "싫어하는 것",
        "value": "미세먼지 · 더운 날씨 · 무례함",
        "note": "나를 불편하게 하는 것을 아는 것도 나를 돌보는 방법이에요.",
        "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=1400&q=85",
        "alt": "부드럽게 밀려오는 바다의 파도",
        "caption": "잠시 물러나는 파도",
    },
    {
        "chapter": "일곱 번째 장",
        "heading": "흥미",
        "value": "사물놀이 · 설장구",
        "note": "새로운 호기심은 아직 가 보지 않은 길을 밝혀 주어요.",
        "image": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=1400&q=85",
        "alt": "아침 햇살이 비치는 초원",
        "caption": "호기심이 피어나는 아침",
    },
    {
        "chapter": "여덟 번째 장",
        "heading": "MBTI",
        "value": "ISFP",
        "note": "나를 알아가는 여러 가지 단서 중 하나를 살며시 펼쳐 봐요.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1400&q=85",
        "alt": "넓게 펼쳐진 초록 들판",
        "caption": "나만의 색으로 물든 들판",
    },
    {
        "chapter": "아홉 번째 장",
        "heading": "꿈",
        "value": "정교하고 자유로운 음악",
        "note": "마음속에 오래 품어 온 바람은 어느새 길이 되기도 해요.",
        "image": "https://images.unsplash.com/photo-1473116763249-2faaef81ccda?auto=format&fit=crop&w=1400&q=85",
        "alt": "구름 사이로 보이는 맑은 하늘",
        "caption": "마음속에 그려 둔 하늘",
    },
    {
        "chapter": "열 번째 장",
        "heading": "장래 희망",
        "value": "초등학교 선생님",
        "note": "천천히 자라날 내일의 모습을 상상하며 마지막 장을 열어요.",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1400&q=85",
        "alt": "햇빛을 받은 산과 능선",
        "caption": "다음 이야기로 이어지는 길",
    },
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gowun+Dodum&display=swap');

    :root {
        --ink: #263d32;
        --moss: #526d52;
        --sage: #dce5d2;
        --paper: #f7f5eb;
        --clay: #b86f52;
    }
    .stApp {
        color: var(--ink);
        background-color: var(--paper);
        background-image: repeating-linear-gradient(135deg, rgba(91, 112, 78, .025) 0 1px, transparent 1px 9px);
        font-family: 'Gowun Dodum', sans-serif;
    }
    .main .block-container { max-width: 1120px; padding: 3rem 2rem 4rem; }
    h1, h2, h3, p, span, button { font-family: 'Gowun Dodum', sans-serif; }
    .book-heading { margin: 0 0 2.2rem; padding-bottom: 1.4rem; border-bottom: 1px solid #d5dacb; }
    .book-kicker { color: var(--moss); font-size: .78rem; letter-spacing: .12em; }
    .book-title { margin: .55rem 0 .45rem; color: var(--ink); font-family: 'Gowun Batang', serif; font-size: 2rem; font-weight: 700; }
    .book-subtitle { margin: 0; color: #647064; font-size: 1rem; }
    .story-page {
        display: grid;
        grid-template-columns: minmax(0, 1.08fr) minmax(280px, .92fr);
        align-items: center;
        gap: clamp(2rem, 6vw, 5rem);
        min-height: 430px;
        padding: 1rem 0 2rem;
        animation: appear .5s ease both;
    }
    .story-page.image-right .story-picture { order: 2; }
    .story-picture { position: relative; margin: 0; }
    .story-picture img {
        display: block;
        width: 100%;
        aspect-ratio: 1.18 / 1;
        object-fit: cover;
        border-radius: 3px 42px 3px 42px;
        box-shadow: 14px 14px 0 var(--sage);
    }
    .story-caption { display: block; margin-top: 1rem; color: #687365; font-size: .82rem; }
    .story-copy { max-width: 430px; padding: 1rem 0; }
    .story-chapter { margin: 0 0 1.1rem; color: var(--clay); font-size: .83rem; }
    .story-heading { margin: 0 0 .8rem; color: var(--ink); font-family: 'Gowun Batang', serif; font-size: 1.65rem; font-weight: 700; }
    .story-value { margin: 0; color: var(--moss); font-family: 'Gowun Batang', serif; font-size: 1.35rem; line-height: 1.7; overflow-wrap: anywhere; }
    .story-rule { width: 46px; height: 1px; margin: 1.5rem 0; background: #b7c1ad; }
    .story-note { color: #59665a; font-size: 1rem; line-height: 1.9; }
    .stProgress > div > div > div > div { background-color: var(--moss); }
    .stProgress p { color: #667064; font-size: .82rem; }
    div.stButton > button {
        min-height: 2.8rem;
        border: 1px solid #b9c4b1;
        border-radius: 2px;
        color: var(--ink);
        background: rgba(255, 255, 255, .35);
        transition: background .2s ease, border-color .2s ease;
    }
    div.stButton > button:hover { border-color: var(--moss); color: var(--ink); background: #e7ecdf; }
    div.stButton > button[kind="primary"] { border-color: var(--moss); color: #fffdf6; background: var(--moss); }
    div.stButton > button[kind="primary"]:hover { border-color: #3e5842; background: #3e5842; }
    .book-end { margin-top: 1.5rem; padding-top: 1.2rem; border-top: 1px solid #d5dacb; color: #788073; font-size: .8rem; text-align: center; }
    @keyframes appear { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 720px) {
        .main .block-container { padding: 2rem 1.15rem 3rem; }
        .story-page { grid-template-columns: 1fr; gap: 1.5rem; min-height: auto; padding-top: .5rem; }
        .story-page.image-right .story-picture { order: 0; }
        .story-picture img { aspect-ratio: 1.35 / 1; }
        .story-copy { padding: .3rem 0; }
        .book-title { font-size: 1.7rem; }
    }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="book-heading">
        <p class="book-kicker">MY LITTLE FOREST · PERSONAL STORY</p>
        <h1 class="book-title">나를 만나는 작은 숲</h1>
        <p class="book-subtitle">풀잎 사이로 한 장씩 펼쳐지는 나의 이야기</p>
    </header>
    """,
    unsafe_allow_html=True,
)

if "story_index" not in st.session_state:
    st.session_state.story_index = 0

current_index = st.session_state.story_index
page = story_pages[current_index]
is_image_right = current_index % 2 == 1
image_position = "image-right" if is_image_right else "image-left"

st.progress((current_index + 1) / len(story_pages), text=f"{current_index + 1} / {len(story_pages)}")

st.markdown(
    f"""
    <section class="story-page {image_position}">
        <figure class="story-picture">
            <img src="{page['image']}" alt="{html.escape(page['alt'], quote=True)}">
            <figcaption class="story-caption">{html.escape(page['caption'])}</figcaption>
        </figure>
        <div class="story-copy">
            <p class="story-chapter">{html.escape(page['chapter'])}</p>
            <h2 class="story-heading">{html.escape(page['heading'])}</h2>
            <p class="story-value">{html.escape(page['value'])}</p>
            <div class="story-rule"></div>
            <p class="story-note">{html.escape(page['note'])}</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

previous_column, page_column, next_column = st.columns([1, 1.2, 1])
with previous_column:
    if st.button("← 이전 장", disabled=current_index == 0, use_container_width=True):
        st.session_state.story_index -= 1
        st.rerun()
with page_column:
    st.markdown(f"<div class='book-end'>{html.escape(page['chapter'])} · 나의 이야기</div>", unsafe_allow_html=True)
with next_column:
    next_label = "처음으로 돌아가기" if current_index == len(story_pages) - 1 else "다음 장 →"
    if st.button(next_label, type="primary", use_container_width=True):
        st.session_state.story_index = 0 if current_index == len(story_pages) - 1 else current_index + 1
        st.rerun()
