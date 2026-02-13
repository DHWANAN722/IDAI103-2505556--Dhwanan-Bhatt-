import streamlit as st
import google.generativeai as genai
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="CoachBot AI", layout="wide")

# --- CUSTOM STYLING (Fixed Button Visibility & Dark Theme) ---
st.markdown("""
    <style>
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(to bottom, #000000, #1a0b2e);
        color: white;
    }
    
    /* Make Button Text Visible (Bright White) */
    div.stButton > button {
        background-color: #bb86fc !important;
        color: #000000 !important; /* Black text on purple button for high contrast */
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
    }
    
    div.stButton > button:hover {
        background-color: #ffffff !important;
        color: #1a0b2e !important;
    }

    /* Styling for text inputs and boxes */
    .stTextInput textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #1e1e2f !important;
        color: white !important;
    }
    
    h1, h2, h3 { color: #bb86fc !important; }

    .quote-box {
        background-color: #2e1a47;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #bb86fc;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUN QUOTES ---
quotes = [
    "“It ain’t about how hard you hit. It’s about how hard you can get hit and keep moving forward.” – Rocky Balboa",
    "“Designated for assignment? I’m the best there is!” – Happy Gilmore",
    "“I’ll be back.” – The Terminator (for your next set!)",
    "“Hard work beats talent when talent doesn’t work hard.” – Tim Notke"
]

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ CoachBot Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    temp = st.slider("Coach Creativity", 0.0, 1.0, 0.4)
    st.markdown("---")
    st.markdown(f'<div class="quote-box"><b>Daily Motivation:</b><br>{random.choice(quotes)}</div>', unsafe_allow_html=True)

# --- MAIN UI ---
st.title("⚡ CoachBot AI: NextGen Sports Lab")
st.subheader("Your AI-powered Personal Trainer")

if not api_key:
    st.warning("Please enter your API Key in the sidebar.")
else:
    # CONFIGURATION FIX: Try 'gemini-1.5-flash' if 'gemini-1.5-pro' continues to 404
    # Ensure you use the exact string: 'gemini-1.5-pro'
    genai.configure(api_key=api_key)
    
    # Selecting the model 
    # NOTE: If 1.5-pro fails, 'gemini-1.5-flash' is a highly reliable alternative
    model = genai.GenerativeModel('gemini-1.5-pro')

    col1, col2 = st.columns(2)
    with col1:
        sport = st.selectbox("Your Sport", ["Football", "Cricket", "Basketball", "Athletics"])
        position = st.text_input("Position", placeholder="e.g. Goalkeeper")
    with col2:
        injury = st.text_area("Injury History", value="None")
        goal = st.selectbox("Goal", ["Recovery", "Strength", "Speed", "Tactics"])

    if st.button("GET MY TRAINING PLAN 🚀"):
        prompt = f"As a youth coach, create a {goal} plan for a {sport} {position} with {injury} history."
        
        with st.spinner("Consulting the playbook..."):
            try:
                # The generate_content method is required by the assignment 
                response = model.generate_content(prompt)
                st.markdown("### 📋 Your Personalized Plan")
                st.write(response.text)
            except Exception as e:
                # If 1.5-pro is still not found, try the flash version automatically
                if "404" in str(e):
                    st.info("Switching to Gemini 1.5 Flash for compatibility...")
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                else:
                    st.error(f"Error: {e}")
    

# --- FOOTER ---
st.markdown("---")
st.caption("Developed for NextGen Sports Lab | Powered by Gemini 1.5 Pro")
