import streamlit as st
import google.generativeai as genai
import random

# Configure page
st.set_page_config(
    page_title="CoachBot AI - Smart Fitness Assistant",
    page_icon="🏆",
    layout="wide"
)

# Custom CSS for purple theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #2d0052 50%, #1a0033 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #a78bfa 0%, #e9d5ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: 800;
        letter-spacing: 2px;
    }
    
    .subtitle {
        text-align: center;
        color: #c084fc;
        font-size: 1.2em;
        margin-bottom: 2rem;
    }
    
    .quote-box {
        background: linear-gradient(135deg, #2d0052 0%, #44006b 100%);
        border: 2px solid #7c3aed;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
    }
    
    .quote-text {
        color: #e9d5ff;
        font-style: italic;
        font-size: 1.1em;
        margin-bottom: 10px;
    }
    
    .quote-author {
        color: #a78bfa;
        font-weight: 600;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 700;
        font-size: 1.1em;
        width: 100%;
    }
    
    .stButton>button:hover {
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.6);
    }
    
    h3 {
        color: #e9d5ff !important;
        margin-top: 2rem;
    }
    
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select,
    .stNumberInput>div>div>input,
    .stTextArea>div>div>textarea {
        background: linear-gradient(135deg, #1a0033 0%, #2d0052 100%);
        border: 2px solid #7c3aed;
        color: #e0e0e0;
    }
    
    label {
        color: #e9d5ff !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Motivational quotes
QUOTES = [
    {"text": "It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward.", "author": "— Rocky Balboa"},
    {"text": "Winners never quit, and quitters never win.", "author": "— Friday Night Lights"},
    {"text": "You miss 100% of the shots you don't take.", "author": "— Wayne Gretzky"},
    {"text": "The only place success comes before work is in the dictionary.", "author": "— Vince Lombardi"},
    {"text": "Champions aren't made in gyms. Champions are made from something they have deep inside them—a desire, a dream, a vision.", "author": "— Muhammad Ali"},
    {"text": "Pressure is a privilege.", "author": "— Billie Jean King"},
    {"text": "The pain of discipline weighs ounces while the pain of regret weighs tons.", "author": "— Jim Rohn"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "— Sam Levenson"},
    {"text": "Excellence is not a destination; it is a continuous journey that never ends.", "author": "— Brian Tracy"},
    {"text": "Your body achieves what your mind believes.", "author": "— Anonymous"}
]

# Initialize session state
if 'quote_index' not in st.session_state:
    st.session_state.quote_index = random.randint(0, len(QUOTES) - 1)
if 'plan_generated' not in st.session_state:
    st.session_state.plan_generated = False

# Configure Gemini API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API Key not configured. Please add your Gemini API key to secrets.toml")
    st.stop()

# Header
st.markdown('<h1 class="main-header">🏆 COACHBOT AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Smart Fitness Assistant</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎬 Inspiration")
    
    # Quote display
    current_quote = QUOTES[st.session_state.quote_index]
    st.markdown(f"""
    <div class="quote-box">
        <div class="quote-text">"{current_quote['text']}"</div>
        <div class="quote-author">{current_quote['author']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 New Quote"):
        st.session_state.quote_index = (st.session_state.quote_index + 1) % len(QUOTES)
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 💪 About CoachBot")
    st.markdown("""
    Your personal AI fitness coach, powered by advanced intelligence. 
    Get tailored workout plans, nutrition guides, and injury prevention tips!
    """)
    
    st.markdown("### 🎯 Features")
    st.markdown("""
    - ✨ Personalized Plans
    - 📊 Tactical Advice
    - 🥗 Nutrition Guides
    - 🛡️ Safety Tips
    - 🔥 Motivation
    """)

# Main form
st.markdown("### 📋 Tell Us About Yourself")

col1, col2 = st.columns(2)

with col1:
    sport = st.text_input("🏅 Your Sport", placeholder="e.g., Basketball, Soccer, Tennis")
    age = st.number_input("📅 Your Age", min_value=13, max_value=100, value=18)
    intensity = st.selectbox("💥 Training Intensity", 
                             ["", "Low (Beginner/Recovery)", "Moderate (Intermediate)", "High (Advanced)"])

with col2:
    position = st.text_input("🎯 Your Position/Role", placeholder="e.g., Center, Midfielder, Pitcher")
    diet = st.selectbox("🥗 Diet Preference", 
                       ["", "Vegetarian", "Non-Vegetarian", "Vegan"])
    goal = st.text_input("🎯 Fitness Goal", placeholder="e.g., Build Strength, Improve Speed")

injuries = st.text_area("🏥 Injury History (Optional)", 
                        placeholder="Any past injuries or current pain? (Leave blank if none)")

# Generate button
if st.button("🚀 Generate My Game Plan"):
    # Validation
    if not all([sport, position, age, intensity, diet, goal]):
        st.error("⚠️ Please fill in all required fields!")
    else:
        st.session_state.plan_generated = True
        
        with st.spinner("⚡ CoachBot is creating your personalized plan..."):
            # Create prompt for Gemini
            prompt = f"""
You are CoachBot AI, an expert fitness coach. Create a comprehensive, personalized fitness plan for:

**Athlete Profile:**
- Sport: {sport}
- Position/Role: {position}
- Age: {age}
- Training Intensity: {intensity}
- Diet Preference: {diet}
- Fitness Goal: {goal}
- Injury History: {injuries if injuries else "None"}

Please provide a detailed plan with these 5 sections:

1. **WORKOUT PLAN**: Weekly schedule with specific exercises, sets, reps, and rest days tailored to their sport and intensity level.

2. **TACTICAL ADVICE**: Sport-specific strategies for their position, including positioning, game IQ, communication, and skills to develop.

3. **NUTRITION GUIDE**: Detailed meal plan based on their diet preference, including pre-workout, post-workout meals, hydration goals, and specific food recommendations.

4. **INJURY PREVENTION**: Warm-up protocols, stretching routines, proper form tips, and recovery strategies. {f"Pay special attention to their injury history: {injuries}" if injuries else "Focus on general injury prevention."}

5. **MOTIVATION**: An inspiring, personalized message that addresses their specific goal and situation. Make it energetic and empowering!

Format each section clearly with bullet points where appropriate. Be specific and actionable.
"""
            
            try:
                # Generate response from Gemini
                response = model.generate_content(prompt)
                plan_text = response.text
                
                # Parse the response into sections
                sections = {
                    "workout": "",
                    "tactical": "",
                    "nutrition": "",
                    "injury": "",
                    "motivation": ""
                }
                
                current_section = None
                for line in plan_text.split('\n'):
                    if 'WORKOUT PLAN' in line.upper():
                        current_section = 'workout'
                    elif 'TACTICAL ADVICE' in line.upper():
                        current_section = 'tactical'
                    elif 'NUTRITION GUIDE' in line.upper():
                        current_section = 'nutrition'
                    elif 'INJURY PREVENTION' in line.upper():
                        current_section = 'injury'
                    elif 'MOTIVATION' in line.upper():
                        current_section = 'motivation'
                    elif current_section:
                        sections[current_section] += line + '\n'
                
                # Store in session state
                st.session_state.plan = sections
                
            except Exception as e:
                st.error(f"Error generating plan: {str(e)}")
                st.session_state.plan_generated = False

# Display results
if st.session_state.plan_generated and 'plan' in st.session_state:
    st.markdown("---")
    st.markdown("## 📊 Your Personalized Game Plan")
    
    # Workout Plan
    with st.expander("🏋️ WORKOUT PLAN", expanded=True):
        st.markdown(st.session_state.plan['workout'])
    
    # Tactical Advice
    with st.expander("🧠 TACTICAL ADVICE", expanded=True):
        st.markdown(st.session_state.plan['tactical'])
    
    # Nutrition Guide
    with st.expander("🥗 NUTRITION GUIDE", expanded=True):
        st.markdown(st.session_state.plan['nutrition'])
    
    # Injury Prevention
    with st.expander("🛡️ INJURY PREVENTION", expanded=True):
        st.markdown(st.session_state.plan['injury'])
    
    # Motivation
    with st.expander("🔥 MOTIVATION", expanded=True):
        st.markdown(st.session_state.plan['motivation'])
