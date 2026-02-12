import streamlit as st
import google.generativeai as genai
import random

# -------------------------------
# CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="CoachBot AI",
    page_icon="🏆",
    layout="wide"
)

# Dark Purple + Black Theme Styling
st.markdown("""
    <style>
    body {
        background-color: #0f0f1a;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #0f0f1a, #1a0033);
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #1f1f2e;
        color: white;
    }
    .stTextArea > div > div > textarea {
        background-color: #1f1f2e;
        color: white;
    }
    .stButton>button {
        background-color: #8000ff;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# GEMINI SETUP
# -------------------------------

genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel(
    "gemini-1.5-pro",
    generation_config={
        "temperature": 0.4,
        "top_p": 0.9
    }
)

# -------------------------------
# FUN QUOTES SECTION
# -------------------------------

quotes = [
    "“It ain’t about how hard you hit. It’s about how hard you can get hit and keep moving forward.” – Rocky",
    "“Clear eyes, full hearts, can’t lose.” – Friday Night Lights",
    "“You miss 100% of the shots you don’t take.” – Wayne Gretzky",
    "“Pain is temporary. Pride is forever.”",
    "“Hard work beats talent when talent doesn’t work hard.”"
]

st.sidebar.title("🎬 Motivation Corner")
st.sidebar.write(random.choice(quotes))
st.sidebar.write("💪 Powered by caffeine and questionable life choices.")

# -------------------------------
# MAIN TITLE
# -------------------------------

st.title("🏆 CoachBot AI")
st.subheader("Your slightly dramatic AI Sports Coach")

st.write("Train smarter. Recover safer. Dominate legally.")

# -------------------------------
# INPUT SECTION
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    sport = st.text_input("🏈 Sport")
    position = st.text_input("🎯 Position")
    goal = st.text_input("🔥 Main Goal")

with col2:
    injury = st.text_input("🩹 Injury History")
    diet = st.text_input("🥗 Diet Preference")
    intensity = st.selectbox("⚡ Training Intensity", ["Low", "Moderate", "High"])

feature = st.selectbox(
    "🎯 What do you need today?",
    [
        "Full Training Plan",
        "Injury Recovery Plan",
        "Nutrition Guide",
        "Tactical Advice",
        "Mental Preparation Routine",
        "Warm-up & Cooldown Plan"
    ]
)

# -------------------------------
# GENERATE BUTTON
# -------------------------------

if st.button("🚀 Generate My Plan"):

    if not sport or not position:
        st.warning("Tell me at least your sport and position. I’m good, not psychic.")
    else:
        prompt = f"""
        You are a professional youth sports coach.

        Athlete Profile:
        Sport: {sport}
        Position: {position}
        Goal: {goal}
        Injury: {injury}
        Diet: {diet}
        Intensity Level: {intensity}

        Generate a {feature}.

        Keep the advice:
        - Safe for teenagers
        - Practical
        - Structured with headings
        - Motivating but not unrealistic
        - Scientifically sound

        Include:
        - Clear steps
        - Duration
        - Safety notes
        - Injury prevention tips if relevant
        """

        with st.spinner("Analyzing your greatness..."):
            response = model.generate_content(prompt)

        st.success("Here’s your custom AI coaching plan 👇")
        st.markdown(response.text)

        st.info("Remember: AI is smart. But listen to your real coach and your body too.")

# -------------------------------
# FOOTER
# -------------------------------

st.markdown("---")
st.markdown("Built with ❤️ + Gemini 1.5 Pro")
st.markdown("If this plan feels too easy, you're either elite or lying about intensity.")
