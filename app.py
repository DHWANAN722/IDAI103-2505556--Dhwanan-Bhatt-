import streamlit as st
import google.generativeai as genai
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="CoachBot AI", layout="wide")

# --- CUSTOM UI STYLING ---
st.markdown("""
    <style>
    /* Dark Purple / Black Background */
    .stApp {
        background: linear-gradient(180deg, #000000 0%, #2D0B4B 100%);
        color: white;
    }
    
    /* FIX: Button Visibility - Black text on bright purple background */
    div.stButton > button {
        background-color: #BB86FC !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 2px solid #BB86FC !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
    }
    
    div.stButton > button:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #ffffff !important;
    }

    /* Input box styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1A1A1A !important;
        color: white !important;
    }

    /* Sidebar Quote Styling */
    .quote-style {
        background-color: #3D1466;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #BB86FC;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUN QUOTES ---
fun_quotes = [
    "“It ain’t about how hard you hit. It’s about how hard you can get hit and keep moving forward.” – Rocky Balboa",
    "“Designated for assignment? I’m the best there is!” – Happy Gilmore",
    "“Winning isn’t everything, it’s the only thing.” – Vince Lombardi",
    "“I’ll be back.” – Terminator (for your next set)",
    "“Just keep swimming.” – Dory",
    "“May the Force be with your gains.” – Star Wars"
]

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    
    st.markdown("---")
    st.markdown(f'<div class="quote-style">{random.choice(fun_quotes)}</div>', unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.title("⚡ CoachBot AI")
st.write("Developing the next generation of athletes with AI-driven training.")

if not api_key:
    st.info("Please enter your API key in the sidebar to start training.")
else:
    try:
        genai.configure(api_key=api_key)
        # Using gemini-1.5-flash to avoid the 404 error
        model = genai.GenerativeModel('gemini-1.5-flash')

        col1, col2 = st.columns(2)
        with col1:
            sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics", "Rugby"])
            position = st.text_input("Player Position", placeholder="e.g. Midfielder / Bowler")
        with col2:
            injury = st.text_area("Injury History", placeholder="e.g. Knee strain, none")
            goal = st.selectbox("Current Goal", ["Build Stamina", "Speed", "Tactical Skills", "Recovery"])

        if st.button("GENERATE COACHING PLAN 🚀"):
            # Prompt Engineering based on Scenario 2 requirements 
            user_prompt = f"""
            Act as a professional youth sports coach. Create a plan for:
            - Sport: {sport}
            - Position: {position}
            - Goal: {goal}
            - Health/Injury History: {injury}
            
            Provide a workout, tactical advice, and a nutrition tip.
            """
            
            with st.spinner("Coach is writing your playbook..."):
                response = model.generate_content(user_prompt)
                st.subheader("Your AI-Powered Playbook")
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"Error: {e}. Check if your API Key is valid and model name is correct.")
