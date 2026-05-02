import streamlit as st
import random
from gtts import gTTS
import time

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="AI Influencer Reel", page_icon="🔥", layout="centered")

# ---------------- HEADER ---------------- #
st.title("🔥 AI Influencer Reel")
st.markdown("Build viral influencer-style content instantly 🚀")

# ---------------- INPUT ---------------- #
brand_name = st.text_input("🏷 Brand Name", "Vetlands Nutrition")
tagline = st.text_input("💬 Tagline", "Best nutrition for performance")

roast_level = st.selectbox(
    "🔥 Roast Level",
    ["mild", "medium", "savage"]
)

personality = st.selectbox(
    "🎭 Influencer Style",
    ["Savage GenZ", "Gym Bro", "Luxury Influencer"]
)

# ---------------- ROAST ENGINE ---------------- #
def generate_roast(brand, tagline, level, personality):

    base = {
        "mild": [
            f"{brand} sounds healthy but where’s the excitement?",
            f"{brand} is giving gym starts tomorrow vibes 😄"
        ],
        "medium": [
            f"{brand} said nutrition but forgot flavor 💀",
            f"{brand} got protein but zero personality 😭"
        ],
        "savage": [
            f"{brand} sounds like cows are the target audience 🐄💀",
            f"If boring had a brand name… it’s {brand} 💀"
        ]
    }

    personality_line = {
        "Savage GenZ": f"{brand} trying to go viral but stuck in 2012 😭",
        "Gym Bro": f"{brand} claims gains but where’s the protein bro 💪",
        "Luxury Influencer": f"{brand} trying to look premium but giving budget vibes 💀"
    }

    return (
        " ".join(random.sample(base[level], 2))
        + " "
        + personality_line[personality]
        + f" {brand} said '{tagline}' but forgot to deliver 💀"
    )

# ---------------- GENERATE ---------------- #
if st.button("🚀 Generate Reel"):

    with st.spinner("🎥 Generating viral reel..."):
        time.sleep(2)

    roast = generate_roast(brand_name, tagline, roast_level, personality)

    views = random.randint(500000, 2000000)
    likes = random.randint(50000, 500000)

    # ---------------- OUTPUT ---------------- #
    st.success("🎬 Your AI Reel is Ready!")

    with st.container():
        st.markdown("### 📱 Reel Preview")

        col1, col2 = st.columns([1, 4])

        with col1:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
                width=60
            )

        with col2:
            st.markdown("**ai.influencer**")
            st.caption("🔥 Trending")

        st.markdown("---")

        st.markdown(f"🧑‍🎤 **{roast}**")

        st.markdown("---")

        st.markdown(f"👁 {views:,} views   ❤️ {likes:,} likes")

    # Copy-friendly output
    st.code(roast)

    # ---------------- AUDIO ---------------- #
    tts = gTTS(text=roast)
    audio_file = "reel.mp3"
    tts.save(audio_file)

    st.audio(audio_file)

    # Download
    with open(audio_file, "rb") as f:
        st.download_button(
            "⬇ Download Audio",
            f,
            "reel.mp3"
        )

    # ---------------- INFO ---------------- #
    st.info("💡 Use this to generate engaging social media content for brands instantly.")

    st.success("🔥 Reel Generated Successfully!")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.caption("⚡ Built by Dhruv Sharma | AI Influencer System")