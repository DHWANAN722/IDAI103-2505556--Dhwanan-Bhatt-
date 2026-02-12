import streamlit as st
import google.generativeai as genai
import random

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="CoachBot AI",
    page_icon="🏆",
    layout="wide"
)

# -------------------------------
# DARK THEME STYLING
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0f1a, #1a0033);
    color: white;
}
h1, h2, h3, h4, h5, h6, p, div {
    color: white;
}
.stTextInput input, .stTextArea textarea {
    background-color: #1f1f2e !important;
    color: white !important;
}
.stSelectbox div {
    background-color: #1f1f2e !important;
    color: white !important;
}
.stButton>button {
    background-color: #8000ff;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# API KEY CONFIGURATION
# -------------------------------

# This works for Streamlit Cloud
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API key not found. Add it in Streamlit Secrets.")
    st.stop()

# -------------------------------
# MODEL SETUP (SAFE MODEL)
# -------------------------------

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.4,
        "top_p": 0.9,
        "max_output_tokens": 1024,
    }
)

# -------------------------------
# SIDEBAR MOTIVATION
# -------------------------------

quotes = [
    "It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward.",
    "You miss 100% of the shots you don’t take.",
    "Clear eyes, full hearts, can’t lose.",
    "Pain is temporary. Pride is forever.",
    "Hard work beats talent when talent doesn't work hard."
]

st.sidebar.title("🎬 Motivation Corner")
st.sidebar.write(random.choice(quotes))
st.sidebar.write("Powered by AI and stubborn ambition.")

# -------------------------------
# MAIN TITLE
# -------------------------------

st.title("🏆 CoachBot AI")
st.subheader("Your AI-Powered Sports Coach")

st.write("Train smarter. Recover safer. Improve consistently.")

# -------------------------------
# USER INPUT SECTION
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
    "🎯 What do you need?",
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
        st.warning("Please enter at least your sport and position.")
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

        Generate a structured {feature}.

        Requirements:
        - Safe for teenage athletes
        - Clear headings
        - Step-by-step format
        - Include duration
        - Include safety precautions
        - Include injury prevention tips if relevant
        - Motivating but realistic tone
        """

        try:
            with st.spinner("Creating your personalized coaching plan..."):
                response = model.generate_content(prompt)

            st.success("Your personalized plan is ready 👇")
            st.markdown(response.text)

        except Exception as e:
            st.error("Error generating response. Check API key and model access.")
            st.write(str(e))

# -------------------------------
# FOOTER
# -------------------------------

st.markdown("---")
st.markdown("Built using Streamlit + Gemini 1.5 Flash")

