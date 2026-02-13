import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="CoachBot AI - Your Personal Sports Coach",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful design
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: scale(1.05);
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
    }
    
    .output-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

def generate_response(prompt, api_key, temperature=0.7):
    """Generate response from Gemini AI"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=temperature,
            )
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease check your API key and try again."

# Main app
def main():
    # Sidebar
    with st.sidebar:
        st.title("🏆 CoachBot AI")
        st.markdown("---")
        
        api_key = st.text_input("🔑 Enter Gemini API Key:", type="password", 
                               help="Get your key from: https://aistudio.google.com/app/apikey")
        
        if api_key:
            st.success("✅ API Key entered!")
        else:
            st.warning("⚠️ Enter API key to continue")
        
        st.markdown("---")
        st.info("💡 **CoachBot AI** - Your personal virtual sports coach powered by Google Gemini AI")
        
        st.markdown("### Features")
        st.markdown("""
        - 🏋️ Workout Plans
        - 🩺 Injury Recovery
        - 🎯 Tactical Coaching
        - 🥗 Nutrition Guide
        - 🔥 Warm-up/Cooldown
        - 💧 Hydration Plans
        - 🧠 Mental Training
        - ⚽ Position Drills
        - 🏃 Stamina Building
        - 📊 Performance Analysis
        """)
    
    # Main content
    st.title("🏆 CoachBot AI")
    st.markdown("### Your Personal Sports Coach Powered by Generative AI")
    
    if not api_key:
        st.warning("👈 Please enter your Gemini API key in the sidebar to get started!")
        st.info("Get your free API key from: https://aistudio.google.com/app/apikey")
        st.stop()
    
    # Create tabs
    tabs = st.tabs([
        "🏋️ Workout",
        "🩺 Recovery",
        "🎯 Tactics",
        "🥗 Nutrition",
        "🔥 Warmup",
        "💧 Hydration",
        "🧠 Mental",
        "⚽ Drills",
        "🏃 Stamina",
        "📊 Analysis"
    ])
    
    # Tab 1: Workout Plan
    with tabs[0]:
        st.header("🏋️ Personalized Workout Plan")
        
        col1, col2 = st.columns(2)
        with col1:
            sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"])
            position = st.text_input("Position/Role", "e.g., Striker, Bowler")
        
        with col2:
            age = st.number_input("Age", 10, 25, 15)
            level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
        
        goal = st.text_area("Training Goal", "e.g., Build stamina, improve speed")
        
        if st.button("Generate Workout Plan", key="b1"):
            if position and goal:
                with st.spinner("🔄 Generating workout plan..."):
                    prompt = f"""As an expert sports coach, create a detailed workout plan for a {age}-year-old {position} in {sport}.

Fitness Level: {level}
Goal: {goal}

Provide:
1. Weekly schedule (Monday-Sunday)
2. Specific exercises with sets/reps
3. Position-specific focus areas
4. Progressive overload tips
5. Recovery guidelines

Make it safe and age-appropriate."""
                    
                    response = generate_response(prompt, api_key, 0.7)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill all fields!")
    
    # Tab 2: Injury Recovery
    with tabs[1]:
        st.header("🩺 Injury Recovery Plan")
        
        col1, col2 = st.columns(2)
        with col1:
            sport2 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s2")
            injury = st.text_input("Injury Type", "e.g., Ankle sprain, Knee pain")
        
        with col2:
            stage = st.selectbox("Recovery Stage", [
                "Just injured (1-2 weeks)",
                "Early recovery (2-4 weeks)",
                "Late recovery (1-2 months)",
                "Nearly healed (2+ months)"
            ])
        
        if st.button("Generate Recovery Plan", key="b2"):
            if injury:
                with st.spinner("🔄 Creating recovery plan..."):
                    prompt = f"""As a sports physiotherapist, create a safe recovery plan:

Sport: {sport2}
Injury: {injury}
Stage: {stage}

Provide:
1. Safe exercises
2. Progression plan
3. Warning signs
4. Strengthening exercises
5. Alternative conditioning
6. Timeline to return

Prioritize safety and proper healing."""
                    
                    response = generate_response(prompt, api_key, 0.5)
                    st.warning("⚠️ Always consult a medical professional!")
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify injury!")
    
    # Tab 3: Tactical Coaching
    with tabs[2]:
        st.header("🎯 Tactical Coaching")
        
        col1, col2 = st.columns(2)
        with col1:
            sport3 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s3")
            position3 = st.text_input("Position", "e.g., Midfielder", key="p3")
        
        with col2:
            skill = st.text_input("Skill to Improve", "e.g., Passing accuracy")
        
        if st.button("Get Tactical Advice", key="b3"):
            if position3 and skill:
                with st.spinner("🔄 Generating advice..."):
                    prompt = f"""As an expert {sport3} coach, provide tactical advice for a {position3} to improve {skill}.

Include:
1. Tactical principles
2. Specific drills
3. Game situations
4. Common mistakes
5. Pro player examples
6. Mental approach

Make it practical for youth athletes."""
                    
                    response = generate_response(prompt, api_key, 0.7)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill all fields!")
    
    # Tab 4: Nutrition
    with tabs[3]:
        st.header("🥗 Nutrition Plan")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            age4 = st.number_input("Age", 10, 25, 15, key="a4")
            weight = st.number_input("Weight (kg)", 30, 120, 55)
        
        with col2:
            height = st.number_input("Height (cm)", 120, 220, 165)
            intensity = st.selectbox("Training Intensity", ["Light", "Moderate", "Heavy", "Very Heavy"])
        
        with col3:
            diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan", "Balanced"])
            allergies = st.text_input("Allergies", "e.g., Lactose")
        
        goal4 = st.text_area("Nutrition Goal", "e.g., Build muscle")
        
        if st.button("Generate Nutrition Plan", key="b4"):
            if goal4:
                with st.spinner("🔄 Creating nutrition plan..."):
                    prompt = f"""As a sports nutritionist, create a plan for:

Age: {age4} years
Weight: {weight} kg
Height: {height} cm
Intensity: {intensity}
Diet: {diet}
Allergies: {allergies if allergies else 'None'}
Goal: {goal4}

Provide:
1. Daily calories
2. Macros (protein/carbs/fats)
3. Sample meal plan
4. Pre/post-workout nutrition
5. Hydration tips
6. Safe supplements
7. Foods to prioritize/avoid

Make it practical and affordable."""
                    
                    response = generate_response(prompt, api_key, 0.6)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify goal!")
    
    # Tab 5: Warmup/Cooldown
    with tabs[4]:
        st.header("🔥 Warm-up & Cooldown")
        
        col1, col2 = st.columns(2)
        with col1:
            sport5 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s5")
            position5 = st.text_input("Position", "e.g., Goalkeeper", key="p5")
        
        with col2:
            session = st.selectbox("Session Type", ["Training", "Match Day", "Light Practice", "Intense Training"])
        
        if st.button("Generate Routines", key="b5"):
            if position5:
                with st.spinner("🔄 Creating routines..."):
                    prompt = f"""As a conditioning coach, create warm-up and cooldown routines for a {position5} in {sport5} for {session}.

WARM-UP (15-20 min):
1. General warm-up
2. Dynamic stretching
3. Sport-specific movements
4. Position drills

COOLDOWN (10-15 min):
1. Light aerobic
2. Static stretching
3. Foam rolling
4. Recovery tips

Include clear instructions and timing."""
                    
                    response = generate_response(prompt, api_key, 0.6)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify position!")
    
    # Tab 6: Hydration
    with tabs[5]:
        st.header("💧 Hydration Strategy")
        
        col1, col2 = st.columns(2)
        with col1:
            sport6 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s6")
            duration = st.slider("Training Duration (hours)", 1, 4, 2)
        
        with col2:
            climate = st.selectbox("Climate", ["Cool", "Moderate", "Hot", "Very Hot/Humid"])
            sweat = st.selectbox("Sweat Rate", ["Low", "Medium", "High"])
        
        if st.button("Generate Hydration Plan", key="b6"):
            with st.spinner("🔄 Creating hydration strategy..."):
                prompt = f"""As a sports nutritionist, create hydration strategy for:

Sport: {sport6}
Duration: {duration} hours
Climate: {climate}
Sweat Rate: {sweat}

Provide:
1. Daily water intake
2. Pre-training protocol
3. During-training schedule
4. Post-training rehydration
5. Electrolyte recommendations
6. Dehydration signs
7. Competition day hydration
8. DIY sports drink recipe

Make it practical."""
                
                response = generate_response(prompt, api_key, 0.6)
                st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
    
    # Tab 7: Mental Training
    with tabs[6]:
        st.header("🧠 Mental Training")
        
        col1, col2 = st.columns(2)
        with col1:
            sport7 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s7")
            situation = st.selectbox("Situation", [
                "Before Important Match",
                "During Competition",
                "After Loss",
                "Dealing with Pressure",
                "Maintaining Consistency"
            ])
        
        with col2:
            challenge = st.text_area("Mental Challenge", "e.g., Pre-match anxiety")
        
        if st.button("Get Mental Coaching", key="b7"):
            if challenge:
                with st.spinner("🔄 Generating mental strategies..."):
                    prompt = f"""As a sports psychologist, provide mental training for a {sport7} athlete:

Situation: {situation}
Challenge: {challenge}

Provide:
1. Visualization techniques
2. Pre-competition routine
3. Mindfulness exercises
4. Positive self-talk
5. Pressure management
6. Building resilience
7. Daily mental routine (5-10 min)

Make it practical for youth athletes."""
                    
                    response = generate_response(prompt, api_key, 0.7)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please describe challenge!")
    
    # Tab 8: Position Drills
    with tabs[7]:
        st.header("⚽ Position Drills")
        
        col1, col2 = st.columns(2)
        with col1:
            sport8 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s8")
            position8 = st.text_input("Position", "e.g., Striker", key="p8")
        
        with col2:
            skill8 = st.text_input("Skill", "e.g., Shooting accuracy")
            equipment = st.multiselect("Equipment", ["Cones", "Ball", "Ladder", "Hurdles", "Bands", "Net", "Partner", "Wall"])
        
        if st.button("Generate Drills", key="b8"):
            if position8 and skill8:
                with st.spinner("🔄 Creating drills..."):
                    prompt = f"""As an expert {sport8} coach, create drills for a {position8} to improve {skill8}.

Equipment: {', '.join(equipment) if equipment else 'Minimal'}

Provide:
1. 5-6 progressive drills
2. Setup instructions
3. Coaching points
4. Common mistakes
5. Sets/reps/duration
6. Progress tracking
7. Difficulty variations

Make drills practical and engaging."""
                    
                    response = generate_response(prompt, api_key, 0.7)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill all fields!")
    
    # Tab 9: Stamina Building
    with tabs[8]:
        st.header("🏃 Stamina Building")
        
        col1, col2 = st.columns(2)
        with col1:
            sport9 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s9")
            current = st.selectbox("Current Endurance", [
                "Can't complete full match",
                "Gets tired in second half",
                "Average endurance",
                "Good, want to excel"
            ])
        
        with col2:
            time_available = st.selectbox("Training Time", ["30 min/day", "45 min/day", "1 hour/day", "1.5 hours/day"])
            weeks = st.slider("Program Duration (weeks)", 4, 12, 8)
        
        if st.button("Generate Stamina Program", key="b9"):
            with st.spinner("🔄 Creating stamina program..."):
                prompt = f"""As a conditioning coach, create a {weeks}-week stamina program for {sport9}:

Current: {current}
Time: {time_available}

Provide:
1. Week-by-week progression
2. Cardio exercises
3. Interval training
4. Sport-specific conditioning
5. Recovery weeks
6. Progress milestones
7. Nutrition tips
8. Overtraining signs

Make it progressive and safe."""
                
                response = generate_response(prompt, api_key, 0.6)
                st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
    
    # Tab 10: Performance Analysis
    with tabs[9]:
        st.header("📊 Performance Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            sport10 = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Tennis", "Athletics"], key="s10")
            position10 = st.text_input("Position", "e.g., Striker", key="p10")
            current_stats = st.text_area("Current Performance", "e.g., 2 goals per 5 matches")
        
        with col2:
            target_stats = st.text_area("Target Performance", "e.g., 1 goal per match")
            timeframe = st.selectbox("Timeframe", ["1 month", "3 months", "6 months", "1 year"])
        
        if st.button("Analyze Performance", key="b10"):
            if position10 and current_stats and target_stats:
                with st.spinner("🔄 Analyzing performance..."):
                    prompt = f"""As a performance analyst, analyze a {position10} in {sport10}:

Current: {current_stats}
Target: {target_stats}
Timeframe: {timeframe}

Provide:
1. Gap analysis
2. Key improvement areas
3. SMART goals
4. Action steps
5. Training focus
6. Tracking metrics
7. Realistic milestones
8. Potential obstacles

Make it realistic and achievable."""
                    
                    response = generate_response(prompt, api_key, 0.7)
                    st.markdown(f'<div class="output-card">{response}</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill all fields!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 1rem;'>
        <p>🏆 <strong>CoachBot AI</strong> - Empowering Young Athletes with AI-Powered Coaching</p>
        <p>Powered by Google Gemini 1.5 Flash | Built with Streamlit</p>
        <p style='font-size: 0.9rem;'>⚠️ Always consult qualified coaches and medical professionals</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
