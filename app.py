import streamlit as st
import google.generativeai as genai

# -------------------------
# PAGE SETUP
# -------------------------
st.set_page_config(page_title="Elite Sports AI", layout="wide")

st.title("🏆 Elite Sports Performance AI")
st.write("Generate a complete, structured training plan using Gemini AI.")

# -------------------------
# GEMINI API KEY INPUT
# -------------------------
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if not api_key:
    st.info("Please enter your Gemini API key to continue.")
    st.stop()

try:
    genai.configure(api_key=api_key)
except:
    st.error("Invalid API Key format.")
    st.stop()

# -------------------------
# USER INPUTS
# -------------------------
sport = st.text_input("Sport")
position = st.text_input("Position")
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
goal = st.text_area("Main Goal")

# -------------------------
# GENERATE BUTTON
# -------------------------
if st.button("Generate Plan"):

    if not sport or not position or not goal:
        st.warning("Please fill in all fields.")
        st.stop()

    with st.spinner("Building your elite training plan..."):

        try:
            model = genai.GenerativeModel("gemini-pro")

            prompt = f"""
You are an elite sports performance coach.

Create a COMPLETE, detailed training plan.

Sport: {sport}
Position: {position}
Experience Level: {experience}
Main Goal: {goal}

Include:
1. Weekly training schedule
2. Strength program
3. Conditioning drills
4. Skill development
5. Recovery strategy
6. Nutrition guidance
7. Mental performance training
8. Weekly progression strategy

Make it detailed and specific.
Avoid generic advice.
"""

            response = model.generate_content(prompt)

            st.markdown("## 📋 Your Personalized Plan")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong. Check your Gemini API key and try again.")
