import streamlit as st
from openai import OpenAI
import random

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Elite Sports AI", page_icon="🏆", layout="wide")

# -----------------------------
# CUSTOM DARK THEME
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f001f, #1a0033, #2b0057);
        color: white;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    .quote-box {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 14px;
        opacity: 0.7;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# FUN SPORTS QUOTES
# -----------------------------
quotes = [
    "Hard work beats talent when talent doesn't work hard.",
    "Pain is temporary. Victory screenshots last forever.",
    "You miss 100% of the shots you don’t take.",
    "Leg day builds character. And fear.",
    "Champions train. Everyone else explains."
]

st.markdown(f"<div class='quote-box'>🏀 {random.choice(quotes)}</div>", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.title("🏆 Elite Sports Performance AI")
st.subheader("Build your personalized domination plan.")

# -----------------------------
# API KEY INPUT
# -----------------------------
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # -----------------------------
    # USER INPUTS
    # -----------------------------
    sport = st.text_input("Sport")
    position = st.text_input("Position")
    experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_area("Main Goal (Be specific)")

    if st.button("Generate Elite Plan 🚀"):

        if sport and position and goal:

            with st.spinner("Building your elite training blueprint..."):

                prompt = f"""
You are an elite-level strength and conditioning coach.

Create a COMPLETE, detailed, structured performance training plan.

Athlete Profile:
Sport: {sport}
Position: {position}
Experience: {experience}
Main Goal: {goal}

The response MUST include:
1. Weekly training split
2. Strength program
3. Conditioning plan
4. Skill development drills
5. Recovery strategy
6. Mental toughness training
7. Nutrition guidance
8. Weekly progression strategy

Make it detailed, specific, and tailored to the sport.
Avoid generic advice.
Make it motivational but professional.
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a high-performance sports coach AI that gives structured, elite-level plans."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.9,
                    max_tokens=1500
                )

                output = response.choices[0].message.content
                st.markdown("## 📋 Your Personalized Plan")
                st.write(output)

        else:
            st.warning("Fill out all fields before generating your plan.")
else:
    st.info("Enter your API key above to unlock the app.")
