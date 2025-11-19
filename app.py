import streamlit as st

# ----------- CONFIG -----------
st.set_page_config(
    page_title="RNG Ikan Roblox – Secret Chance",
    page_icon="🐟",
    layout="centered"
)

# ----------- CUSTOM CSS -----------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #71b7e6, #9b59b6);
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: 900;
        color: #fff;
        text-shadow: 1px 1px 3px #000;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        margin-top: -10px;
        font-size: 18px;
    }
    .card {
        background: rgba(255,255,255,0.15);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        backdrop-filter: blur(8px);
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        background: rgba(255,255,255,0.2);
        font-size: 22px;
        font-weight: 700;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- TITLE -----------
st.markdown("<div class='title'>🐟 RNG Ikan Roblox</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Hitung peluang Secret (1% – 100%)</div><br>", unsafe_allow_html=True)

# ----------- INPUT -----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📥 Input Jumlah Ikan")

legend = st.number_input("Legendary", min_value=0, value=5)
epic = st.number_input("Epic", min_value=0, value=10)
rare = st.number_input("Rare", min_value=0, value=20)
mystic = st.number_input("Mitos", min_value=0, value=1)

st.markdown("</div>", unsafe_allow_html=True)

# ----------- CALC -----------
total = legend + epic + rare + mystic

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📊 Hasil Perhitungan")

if total == 0:
    st.warning("Isi jumlah ikan dulu! Pool masih kosong.")
else:
    # hitungan dasar
    base = (1 / total) * 100

    # DIPAKSA 1%–100%
    chance = max(1, min(100, base))

    st.markdown(
        f"<div class='result-box'>🎯 Peluang Secret:<br>"
        f"<span style='font-size:35px'>{chance:.2f}%</span></div>",
        unsafe_allow_html=True
    )
    st.write(f"Total ikan: **{total}**")
    st.caption("Chance dibatasi di rentang 1% – 100%.")

st.markdown("</div>", unsafe_allow_html=True)
