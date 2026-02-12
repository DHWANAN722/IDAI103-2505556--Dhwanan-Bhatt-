import streamlit as st
import google.generativeai as genai
from datetime import datetime

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
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 102, 241, 0.4);
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        padding: 1rem 0;
    }
    
    h2 {
        color: #667eea;
        font-weight: 600;
    }
    
    h3 {
        color: #764ba2;
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

# Configure Gemini AI
def configure_gemini(api_key):
    """Configure Gemini AI with the provided API key"""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"Error configuring Gemini AI: {str(e)}")
        return False

def generate_ai_response(prompt, temperature=0.7):
    """Generate response from Gemini AI"""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
            )
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Main app
def main():
    # Sidebar for API Key
    with st.sidebar:
        st.title("🏆 CoachBot AI")
        st.markdown("---")
        st.markdown("### Configuration")
        
        api_key = st.text_input("Enter your Gemini API Key:", type="password", 
                               help="Get your API key from https://aistudio.google.com/app/apikey")
        
        if api_key:
            if configure_gemini(api_key):
                st.success("✅ API Key configured successfully!")
            st.session_state['api_configured'] = True
        else:
            st.warning("⚠️ Please enter your Gemini API key to continue")
            st.session_state['api_configured'] = False
        
        st.markdown("---")
        st.markdown("### About")
        st.info("CoachBot AI is your personal virtual sports coach powered by Generative AI. Get personalized training plans, nutrition advice, and tactical coaching!")
        
        st.markdown("---")
        st.markdown("### Features")
        st.markdown("""
        - 🏋️ Custom Workout Plans
        - 🩺 Injury-Safe Training
        - 🎯 Tactical Coaching
        - 🥗 Nutrition Guidance
        - 🧘 Mental Focus Tips
        - ⚽ Sport-Specific Drills
        """)
    
    # Main content
    st.title("🏆 CoachBot AI")
    st.markdown("### Your Personal Sports Coach Powered by Generative AI")
    
    if not st.session_state.get('api_configured', False):
        st.warning("👈 Please enter your Gemini API key in the sidebar to get started!")
        st.stop()
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
        "🏋️ Workout Plan",
        "🩺 Injury Recovery",
        "🎯 Tactical Coaching",
        "🥗 Nutrition Guide",
        "🔥 Warm-up/Cooldown",
        "💧 Hydration Plan",
        "🧠 Mental Focus",
        "⚽ Position Drills",
        "🏃 Stamina Building",
        "📊 Performance Analysis"
    ])
    
    # Tab 1: Workout Plan
    with tab1:
        st.header("🏋️ Generate Personalized Workout Plan")
        col1, col2 = st.columns(2)
        
        with col1:
            sport = st.selectbox("Select Your Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ])
            position = st.text_input("Your Position/Role", placeholder="e.g., Striker, Bowler, Point Guard")
        
        with col2:
            age = st.number_input("Your Age", min_value=10, max_value=25, value=15)
            fitness_level = st.select_slider("Current Fitness Level", 
                                            options=["Beginner", "Intermediate", "Advanced"])
        
        training_goal = st.text_area("Training Goal", 
                                     placeholder="e.g., Build stamina, increase speed, improve technique")
        
        if st.button("Generate Workout Plan", key="workout"):
            if position and training_goal:
                with st.spinner("Generating your personalized workout plan..."):
                    prompt = f"""As an expert sports coach, create a detailed and personalized workout plan for a {age}-year-old {position} in {sport}. 
                    
Current fitness level: {fitness_level}
Training goal: {training_goal}

Please provide:
1. A week-long workout schedule (Monday to Sunday)
2. Specific exercises for each day with sets, reps, and duration
3. Focus areas for this position
4. Progressive overload recommendations
5. Rest and recovery guidelines

Make the plan safe, age-appropriate, and effective for a youth athlete."""
                    
                    response = generate_ai_response(prompt, temperature=0.7)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Your Personalized Workout Plan")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields!")
    
    # Tab 2: Injury Recovery
    with tab2:
        st.header("🩺 Safe Recovery Training Plan")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_injury = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_injury")
            
            injury_type = st.text_input("Type of Injury", placeholder="e.g., Ankle sprain, Knee strain, Shoulder pain")
        
        with col2:
            recovery_stage = st.selectbox("Recovery Stage", [
                "Just injured (1-2 weeks)",
                "Early recovery (2-4 weeks)",
                "Late recovery (1-2 months)",
                "Nearly healed (2+ months)"
            ])
        
        if st.button("Generate Recovery Plan", key="injury"):
            if injury_type:
                with st.spinner("Creating your safe recovery plan..."):
                    prompt = f"""As a sports physiotherapist and coach, create a safe recovery training plan for an athlete with the following condition:

Sport: {sport_injury}
Injury: {injury_type}
Recovery Stage: {recovery_stage}

Please provide:
1. Safe exercises that avoid aggravating the injury
2. Gradual progression plan back to full training
3. Warning signs to watch for
4. Exercises to strengthen the affected area
5. Alternative conditioning methods during recovery
6. Estimated timeline to return to sport

Make sure all recommendations prioritize safety and proper healing."""
                    
                    response = generate_ai_response(prompt, temperature=0.5)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Your Safe Recovery Plan")
                    st.warning("⚠️ Always consult with a medical professional before starting any recovery program!")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify your injury!")
    
    # Tab 3: Tactical Coaching
    with tab3:
        st.header("🎯 Tactical Coaching & Skill Improvement")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_tactical = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_tactical")
            
            position_tactical = st.text_input("Position", placeholder="e.g., Midfielder, Fast Bowler, Shooting Guard", key="pos_tactical")
        
        with col2:
            skill_focus = st.text_input("Skill to Improve", placeholder="e.g., Passing accuracy, Swing bowling, Three-point shooting")
        
        if st.button("Get Tactical Advice", key="tactical"):
            if position_tactical and skill_focus:
                with st.spinner("Generating tactical coaching advice..."):
                    prompt = f"""As an expert {sport_tactical} coach, provide tactical coaching advice for a {position_tactical} to improve their {skill_focus}.

Please include:
1. Key tactical principles for this position
2. Specific drills to practice the skill
3. Game situations where this skill is crucial
4. Common mistakes to avoid
5. Professional player examples to study
6. Mental approach and decision-making tips

Make the advice practical and actionable for a youth athlete."""
                    
                    response = generate_ai_response(prompt, temperature=0.7)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Tactical Coaching Advice")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields!")
    
    # Tab 4: Nutrition Guide
    with tab4:
        st.header("🥗 Personalized Nutrition Plan")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            age_nutrition = st.number_input("Age", min_value=10, max_value=25, value=15, key="age_nut")
            weight = st.number_input("Weight (kg)", min_value=30, max_value=120, value=55)
        
        with col2:
            height = st.number_input("Height (cm)", min_value=120, max_value=220, value=165)
            activity_level = st.select_slider("Training Intensity", 
                                             options=["Light", "Moderate", "Heavy", "Very Heavy"])
        
        with col3:
            diet_type = st.selectbox("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Balanced"])
            allergies = st.text_input("Allergies/Restrictions", placeholder="e.g., Lactose intolerant, No seafood")
        
        goal_nutrition = st.text_area("Nutrition Goal", placeholder="e.g., Build muscle, Lose weight, Increase energy")
        
        if st.button("Generate Nutrition Plan", key="nutrition"):
            if goal_nutrition:
                with st.spinner("Creating your personalized nutrition plan..."):
                    prompt = f"""As a sports nutritionist, create a detailed nutrition plan for a young athlete with the following profile:

Age: {age_nutrition} years
Weight: {weight} kg
Height: {height} cm
Training Intensity: {activity_level}
Diet Type: {diet_type}
Allergies/Restrictions: {allergies if allergies else "None"}
Goal: {goal_nutrition}

Please provide:
1. Daily calorie requirements
2. Macronutrient breakdown (protein, carbs, fats)
3. Sample meal plan for one day (breakfast, lunch, dinner, snacks)
4. Pre-workout and post-workout nutrition
5. Hydration recommendations
6. Supplements if needed (safe for youth)
7. Foods to prioritize and avoid

Make it practical, affordable, and suitable for a young athlete."""
                    
                    response = generate_ai_response(prompt, temperature=0.6)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Your Personalized Nutrition Plan")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify your nutrition goal!")
    
    # Tab 5: Warm-up/Cooldown
    with tab5:
        st.header("🔥 Warm-up & Cooldown Routines")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_warmup = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_warmup")
        
        with col2:
            position_warmup = st.text_input("Position", placeholder="e.g., Goalkeeper, Sprinter", key="pos_warmup")
        
        session_type = st.selectbox("Session Type", [
            "Training Session",
            "Match Day",
            "Light Practice",
            "Intense Training"
        ])
        
        if st.button("Generate Routines", key="warmup"):
            if position_warmup:
                with st.spinner("Generating warm-up and cooldown routines..."):
                    prompt = f"""As a sports conditioning coach, create comprehensive warm-up and cooldown routines for a {position_warmup} in {sport_warmup} preparing for a {session_type}.

Please provide:

**WARM-UP ROUTINE (15-20 minutes):**
1. General warm-up (5-7 minutes)
2. Dynamic stretching (5-7 minutes)
3. Sport-specific movements (5-7 minutes)
4. Position-specific activation drills

**COOLDOWN ROUTINE (10-15 minutes):**
1. Light aerobic cooldown (3-5 minutes)
2. Static stretching routine (5-7 minutes)
3. Foam rolling recommendations (3-5 minutes)
4. Recovery tips

Make it specific to the sport and position, with clear instructions and timing."""
                    
                    response = generate_ai_response(prompt, temperature=0.6)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Your Warm-up & Cooldown Routines")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please specify your position!")
    
    # Tab 6: Hydration Plan
    with tab6:
        st.header("💧 Hydration & Electrolyte Strategy")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_hydration = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_hydration")
            
            training_duration = st.slider("Training Duration (hours)", 1, 4, 2)
        
        with col2:
            climate = st.selectbox("Climate", ["Cool", "Moderate", "Hot", "Very Hot/Humid"])
            sweat_rate = st.select_slider("Sweat Rate", options=["Low", "Medium", "High"])
        
        if st.button("Generate Hydration Plan", key="hydration"):
            with st.spinner("Creating your hydration strategy..."):
                prompt = f"""As a sports nutritionist, create a detailed hydration and electrolyte strategy for an athlete with the following profile:

Sport: {sport_hydration}
Training Duration: {training_duration} hours
Climate: {climate}
Sweat Rate: {sweat_rate}

Please provide:
1. Total daily water intake recommendation
2. Pre-training hydration protocol (timing and amount)
3. During-training hydration schedule
4. Post-training rehydration strategy
5. Electrolyte replacement recommendations
6. Signs of dehydration to watch for
7. Hydration for competition day
8. DIY sports drink recipe if applicable

Make it practical and specific to the conditions."""
                
                response = generate_ai_response(prompt, temperature=0.6)
                
                st.markdown('<div class="output-card">', unsafe_allow_html=True)
                st.markdown("### Your Hydration Strategy")
                st.markdown(response)
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Tab 7: Mental Focus
    with tab7:
        st.header("🧠 Mental Focus & Visualization Training")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_mental = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_mental")
            
            situation = st.selectbox("Situation", [
                "Before Important Match",
                "During Competition",
                "After Loss/Failure",
                "Dealing with Pressure",
                "Maintaining Consistency"
            ])
        
        with col2:
            challenge = st.text_area("Mental Challenge", 
                                    placeholder="e.g., Getting nervous before penalties, Losing focus in second half")
        
        if st.button("Get Mental Coaching", key="mental"):
            if challenge:
                with st.spinner("Generating mental training strategies..."):
                    prompt = f"""As a sports psychologist, provide mental training and visualization techniques for a {sport_mental} athlete facing this challenge:

Situation: {situation}
Challenge: {challenge}

Please provide:
1. Visualization techniques specific to their sport
2. Pre-competition mental preparation routine
3. Mindfulness and focus exercises
4. Positive self-talk strategies
5. Pressure management techniques
6. Building mental resilience
7. Daily mental training routine (5-10 minutes)

Make it practical and age-appropriate for youth athletes."""
                    
                    response = generate_ai_response(prompt, temperature=0.7)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Mental Training Program")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please describe your mental challenge!")
    
    # Tab 8: Position Drills
    with tab8:
        st.header("⚽ Position-Specific Drills & Exercises")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_drills = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_drills")
            
            position_drills = st.text_input("Position", placeholder="e.g., Central Midfielder, Spin Bowler", key="pos_drills")
        
        with col2:
            skill_drills = st.text_input("Skill to Practice", placeholder="e.g., First touch, Yorker delivery, Defensive footwork")
            equipment = st.multiselect("Available Equipment", [
                "Cones", "Ball", "Ladder", "Hurdles", "Resistance Bands", 
                "Goal/Net", "Training Partner", "Wall"
            ])
        
        if st.button("Generate Drills", key="drills"):
            if position_drills and skill_drills:
                with st.spinner("Creating position-specific drills..."):
                    prompt = f"""As an expert {sport_drills} coach, create position-specific drills for a {position_drills} to improve their {skill_drills}.

Available Equipment: {', '.join(equipment) if equipment else 'Minimal equipment'}

Please provide:
1. 5-6 progressive drills from basic to advanced
2. Clear setup instructions for each drill
3. Key coaching points and technique tips
4. Common mistakes to avoid
5. Sets, reps, and duration for each drill
6. How to track progress
7. Variations to increase difficulty

Make the drills practical, engaging, and effective for skill development."""
                    
                    response = generate_ai_response(prompt, temperature=0.7)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Position-Specific Drills")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields!")
    
    # Tab 9: Stamina Building
    with tab9:
        st.header("🏃 Stamina & Endurance Building Program")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_stamina = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_stamina")
            
            current_level = st.selectbox("Current Endurance Level", [
                "Can't complete full match/game",
                "Gets tired in second half",
                "Average endurance",
                "Good endurance, want to excel"
            ])
        
        with col2:
            time_available = st.selectbox("Training Time Available", [
                "30 minutes/day",
                "45 minutes/day",
                "1 hour/day",
                "1.5 hours/day"
            ])
            
            weeks = st.slider("Program Duration (weeks)", 4, 12, 8)
        
        if st.button("Generate Stamina Program", key="stamina"):
            with st.spinner("Creating your stamina building program..."):
                prompt = f"""As a conditioning coach, create a progressive {weeks}-week stamina and endurance building program for a {sport_stamina} athlete.

Current Level: {current_level}
Training Time: {time_available}

Please provide:
1. Week-by-week progression plan
2. Specific cardio exercises and drills
3. Interval training protocols
4. Sport-specific conditioning
5. Recovery weeks and adaptation periods
6. Measurable milestones to track progress
7. Nutrition tips for endurance
8. Signs of overtraining to watch for

Make it progressive, safe, and effective for building match fitness."""
                
                response = generate_ai_response(prompt, temperature=0.6)
                
                st.markdown('<div class="output-card">', unsafe_allow_html=True)
                st.markdown(f"### Your {weeks}-Week Stamina Building Program")
                st.markdown(response)
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Tab 10: Performance Analysis
    with tab10:
        st.header("📊 Performance Analysis & Goal Setting")
        
        col1, col2 = st.columns(2)
        with col1:
            sport_analysis = st.selectbox("Sport", [
                "Football/Soccer", "Cricket", "Basketball", "Tennis", 
                "Athletics", "Swimming", "Badminton", "Hockey", "Volleyball"
            ], key="sport_analysis")
            
            position_analysis = st.text_input("Position", placeholder="e.g., Striker, Wicket-keeper", key="pos_analysis")
        
        with col2:
            current_stats = st.text_area("Current Performance Stats", 
                                        placeholder="e.g., Scoring 2 goals per 5 matches, bowling average 35")
            
            target_stats = st.text_area("Target Performance", 
                                       placeholder="e.g., Want to score 1 goal per match, bowling average under 25")
        
        timeframe = st.selectbox("Timeframe to Achieve Goal", [
            "1 month", "3 months", "6 months", "1 year"
        ])
        
        if st.button("Analyze Performance", key="analysis"):
            if position_analysis and current_stats and target_stats:
                with st.spinner("Analyzing your performance and creating action plan..."):
                    prompt = f"""As a performance analyst and coach, analyze the performance of a {position_analysis} in {sport_analysis} and create an improvement plan.

Current Performance: {current_stats}
Target Performance: {target_stats}
Timeframe: {timeframe}

Please provide:
1. Gap analysis between current and target performance
2. Key areas that need improvement
3. SMART goals broken down by timeframe
4. Specific action steps to achieve each goal
5. Training focus areas
6. Metrics to track weekly/monthly
7. Realistic expectations and milestones
8. Potential obstacles and how to overcome them

Make the plan realistic, measurable, and achievable within the timeframe."""
                    
                    response = generate_ai_response(prompt, temperature=0.7)
                    
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown("### Performance Analysis & Action Plan")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 2rem 0;'>
        <p>🏆 <strong>CoachBot AI</strong> - Empowering Young Athletes with AI-Powered Coaching</p>
        <p>Powered by Google Gemini 1.5 Pro | Built with Streamlit</p>
        <p style='font-size: 0.9rem;'>⚠️ Always consult with qualified coaches and medical professionals for personalized advice</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
