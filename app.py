import streamlit as st
from openai import OpenAI

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Elite Sports AI", layout="wide")

# -------------------------
# SIMPLE WHITE STYLE
# -------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 Elite Sports Performance AI")
st.write("Generate a complete, structured training plan tailored to you.")

# -------------------------
# API KEY INPUT
# -------------------------
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if not api_key:
    st.info("Please enter your API key to continue.")
    st.stop()

# Create client safely
try:
    client = OpenAI(api_key=api_key)
except Exception as e:
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
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an elite sports performance coach. Give detailed, structured, professional plans. Avoid generic advice."
                    },
                    {
                        "role": "user",
                        "content": f"""
Create a COMPLETE training plan.

Sport: {sport}
Position: {position}
Experience: {experience}
Main Goal: {goal}

Include:
1. Weekly training schedule
2. Strength program
3. Conditioning drills
4. Skill work
5. Recovery strategy
6. Nutrition guidance
7. Mental training
8. Progression plan

Be specific and detailed.
"""
                    }
                ],
                temperature=0.8,
                max_tokens=1800
            )

            output = response.choices[0].message.content
            st.markdown("## 📋 Your Personalized Plan")
            st.write(output)

        except Exception as e:
            st.error("Authentication failed or API error. Double-check your API key.")
