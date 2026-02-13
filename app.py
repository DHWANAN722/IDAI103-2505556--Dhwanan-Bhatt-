import streamlit as st
from openai import OpenAI

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Elite Sports AI", layout="wide")

st.title("🏆 Elite Sports Performance AI")
st.write("Generate a complete, structured, elite-level training plan.")

# -------------------------
# API KEY INPUT
# -------------------------
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if not api_key:
    st.info("Please enter your API key to continue.")
    st.stop()

try:
    client = OpenAI(api_key=api_key)
except Exception:
    st.error("Invalid API key format.")
    st.stop()

# -------------------------
# USER INPUTS
# -------------------------
sport = st.text_input("Sport")
position = st.text_input("Position")
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
goal = st.text_area("Main Goal (be specific)")

# -------------------------
# GENERATE BUTTON
# -------------------------
if st.button("Generate Plan"):

    if not sport or not position or not goal:
        st.warning("Please fill in all fields.")
        st.stop()

    with st.spinner("Creating your elite performance blueprint..."):

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an elite professional strength and conditioning coach. "
                            "You produce detailed, structured, sport-specific training plans. "
                            "Avoid generic advice. Be specific, tactical, and practical."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"""
Create a COMPLETE, highly detailed performance training plan.

Athlete Profile:
Sport: {sport}
Position: {position}
Experience Level: {experience}
Main Goal: {goal}

The response MUST include:

1. Weekly training split (day-by-day)
2. Strength & power program (sets, reps)
3. Conditioning plan
4. Skill-specific drills
5. Recovery strategy
6. Nutrition framework
7. Mental performance training
8. 4-week progression strategy

Make it structured with clear headings.
Be specific to the sport and position.
No vague motivational fluff.
"""
                    }
                ],
                temperature=0.85,
                max_tokens=2000
            )

            output = response.choices[0].message.content

            st.markdown("## 📋 Your Personalized Plan")
            st.write(output)

        except Exception as e:
            st.error("Authentication failed or API issue. Double-check your API key.")

