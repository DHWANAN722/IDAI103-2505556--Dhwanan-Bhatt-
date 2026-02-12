import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import os

# Configure the page
st.set_page_config(
    page_title="ArtRestorer AI",
    page_icon="🎨",
    layout="wide"
)

# Configure Gemini API
# Users need to add their own API key
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to use the app.")

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #8B4513;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #696969;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🎨 ArtRestorer AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Smart Assistance for Art Restoration & Cultural Heritage Preservation</p>', unsafe_allow_html=True)

# Sidebar - Feature Selection
st.sidebar.title("🖼️ Select Feature")
feature = st.sidebar.selectbox(
    "Choose an AI feature:",
    [
        "1. Artwork Analysis & Condition Assessment",
        "2. Restoration Technique Recommendations",
        "3. Historical Context & Provenance Research",
        "4. Symbol & Inscription Interpretation",
        "5. Material Composition Analysis",
        "6. Color Palette Restoration Guidance",
        "7. Museum Exhibition Description Generator",
        "8. Damage Pattern Recognition",
        "9. Conservation Best Practices",
        "10. Virtual Restoration Preview Description"
    ]
)

# Temperature and Top-P settings for model tuning
st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Model Settings")
temperature = st.sidebar.slider("Temperature (Creativity)", 0.0, 1.0, 0.7, 0.1)
top_p = st.sidebar.slider("Top P (Diversity)", 0.0, 1.0, 0.9, 0.1)

# Main content area
if api_key:
    
    # Feature 1: Artwork Analysis & Condition Assessment
    if feature.startswith("1."):
        st.header("🔍 Artwork Analysis & Condition Assessment")
        st.write("Upload an image of an artwork to receive a detailed condition assessment.")
        
        uploaded_file = st.file_uploader("Upload artwork image", type=['png', 'jpg', 'jpeg'])
        artwork_description = st.text_area("Additional details about the artwork (optional):", 
                                          placeholder="E.g., oil painting, approximately 200 years old, stored in humid conditions...")
        
        if st.button("Analyze Artwork"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Artwork", use_container_width=True)
                
                with st.spinner("Analyzing artwork condition..."):
                    prompt = f"""As an expert art conservator, analyze this artwork image and provide a detailed condition assessment including:
                    1. Overall condition rating (Excellent/Good/Fair/Poor)
                    2. Visible damage or deterioration (cracks, discoloration, fading, etc.)
                    3. Areas of concern that need immediate attention
                    4. Estimated age and condition based on visual analysis
                    5. Urgency level for restoration (Low/Medium/High/Critical)
                    
                    Additional context: {artwork_description if artwork_description else 'No additional details provided'}
                    
                    Provide your analysis in a professional, structured format."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Analysis Complete!")
                        st.markdown("### 📋 Condition Assessment Report")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 2: Restoration Technique Recommendations
    elif feature.startswith("2."):
        st.header("🛠️ Restoration Technique Recommendations")
        st.write("Get AI-powered recommendations for restoration techniques based on artwork type and damage.")
        
        artwork_type = st.selectbox("Artwork Type:", 
                                    ["Oil Painting", "Watercolor", "Fresco", "Sculpture", "Textile", "Paper/Manuscript", "Photograph"])
        damage_type = st.multiselect("Type of Damage:", 
                                     ["Cracks", "Fading", "Discoloration", "Tears", "Water Damage", "Mold", "Flaking Paint", "Surface Dirt"])
        artwork_age = st.text_input("Approximate Age:", placeholder="E.g., 18th century, 200 years old")
        
        uploaded_file = st.file_uploader("Upload artwork image (optional)", type=['png', 'jpg', 'jpeg'])
        
        if st.button("Get Recommendations"):
            if damage_type:
                prompt = f"""As a master art restorer, provide detailed restoration technique recommendations for:
                
                Artwork Type: {artwork_type}
                Damage Observed: {', '.join(damage_type)}
                Approximate Age: {artwork_age if artwork_age else 'Not specified'}
                
                Please provide:
                1. Step-by-step restoration approach
                2. Recommended materials and tools
                3. Precautions and risks to be aware of
                4. Estimated timeframe for restoration
                5. Whether professional intervention is required or if basic conservation can be done
                6. Alternative techniques if traditional methods are too risky
                
                Be specific, practical, and culturally sensitive to the artwork's heritage."""
                
                with st.spinner("Generating restoration recommendations..."):
                    try:
                        if uploaded_file:
                            image = Image.open(uploaded_file)
                            st.image(image, caption="Artwork Reference", use_container_width=True)
                            response = model.generate_content(
                                [prompt, image],
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature,
                                    top_p=top_p,
                                )
                            )
                        else:
                            response = model.generate_content(
                                prompt,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature,
                                    top_p=top_p,
                                )
                            )
                        st.success("Recommendations Generated!")
                        st.markdown("### 🎯 Restoration Technique Recommendations")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please select at least one type of damage.")
    
    # Feature 3: Historical Context & Provenance Research
    elif feature.startswith("3."):
        st.header("📚 Historical Context & Provenance Research")
        st.write("Discover the historical background and potential origins of your artwork.")
        
        uploaded_file = st.file_uploader("Upload artwork image", type=['png', 'jpg', 'jpeg'])
        known_info = st.text_area("What do you know about this artwork?", 
                                  placeholder="E.g., found in an estate sale, appears to be European, has signature that looks like...")
        
        if st.button("Research Historical Context"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Artwork for Analysis", use_container_width=True)
                
                with st.spinner("Researching historical context..."):
                    prompt = f"""As an art historian, analyze this artwork and provide insights about:
                    
                    1. Possible time period and artistic movement (Renaissance, Baroque, Impressionism, etc.)
                    2. Regional/cultural origin indicators (style, technique, subject matter)
                    3. Similar known works or artists with comparable styles
                    4. Historical context of the depicted subject or scene
                    5. Potential significance in art history
                    6. Suggestions for further provenance research
                    
                    Known information: {known_info if known_info else 'No prior information provided'}
                    
                    Provide an educational, engaging analysis that helps understand the artwork's place in history."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Research Complete!")
                        st.markdown("### 🏛️ Historical Analysis")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 4: Symbol & Inscription Interpretation
    elif feature.startswith("4."):
        st.header("🔤 Symbol & Inscription Interpretation")
        st.write("Decode symbols, inscriptions, or text found in artworks.")
        
        uploaded_file = st.file_uploader("Upload image with symbols/inscriptions", type=['png', 'jpg', 'jpeg'])
        context = st.text_area("Provide context:", 
                              placeholder="E.g., found on the back of a painting, appears to be Latin, symbols look religious...")
        
        if st.button("Interpret Symbols"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Image with Symbols/Inscriptions", use_container_width=True)
                
                with st.spinner("Interpreting symbols and inscriptions..."):
                    prompt = f"""As an expert in art history, iconography, and ancient languages, analyze the symbols and inscriptions in this image:
                    
                    1. Identify any visible text, symbols, or markings
                    2. Determine the likely language or symbolic system
                    3. Provide translation or interpretation where possible
                    4. Explain cultural or religious significance
                    5. Date the inscription style if possible
                    6. Suggest what the symbols might reveal about the artwork's origin or purpose
                    
                    Context: {context if context else 'No additional context provided'}
                    
                    Be scholarly but accessible in your explanation."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Interpretation Complete!")
                        st.markdown("### 📜 Symbol & Inscription Analysis")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 5: Material Composition Analysis
    elif feature.startswith("5."):
        st.header("🧪 Material Composition Analysis")
        st.write("Get insights into the materials and techniques used to create the artwork.")
        
        uploaded_file = st.file_uploader("Upload artwork image", type=['png', 'jpg', 'jpeg'])
        artwork_info = st.text_area("Artwork details:", 
                                    placeholder="E.g., painting on canvas, appears to have gold leaf, heavy texture...")
        
        if st.button("Analyze Materials"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Artwork", use_container_width=True)
                
                with st.spinner("Analyzing material composition..."):
                    prompt = f"""As a materials science expert specializing in art conservation, analyze this artwork and provide insights about:
                    
                    1. Likely painting medium (oil, acrylic, tempera, watercolor, etc.)
                    2. Canvas or support material characteristics
                    3. Pigments that may have been used (based on colors and time period)
                    4. Special materials detected (gold leaf, varnish, etc.)
                    5. Application techniques visible (impasto, glazing, etc.)
                    6. How materials may have degraded over time
                    7. Conservation implications based on materials
                    
                    Additional details: {artwork_info if artwork_info else 'No details provided'}
                    
                    Explain in a way that helps with restoration planning."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Analysis Complete!")
                        st.markdown("### 🔬 Material Composition Report")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 6: Color Palette Restoration Guidance
    elif feature.startswith("6."):
        st.header("🎨 Color Palette Restoration Guidance")
        st.write("Get recommendations for color matching and restoration to original palette.")
        
        uploaded_file = st.file_uploader("Upload artwork image", type=['png', 'jpg', 'jpeg'])
        fading_areas = st.text_input("Describe faded areas:", 
                                    placeholder="E.g., sky area significantly faded, reds turned brown...")
        
        if st.button("Analyze Color Palette"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Current State of Artwork", use_container_width=True)
                
                with st.spinner("Analyzing color palette..."):
                    prompt = f"""As a color specialist and art restorer, analyze this artwork's color palette and provide:
                    
                    1. Current dominant colors and their condition
                    2. Identification of faded or altered colors
                    3. Likely original color palette based on visible remnants and artistic period
                    4. Specific pigment recommendations for color matching
                    5. Color mixing ratios and techniques
                    6. How to achieve color consistency across restored areas
                    7. Testing recommendations before full application
                    
                    Fading information: {fading_areas if fading_areas else 'General assessment needed'}
                    
                    Provide practical, actionable color restoration guidance."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Analysis Complete!")
                        st.markdown("### 🌈 Color Palette Restoration Guide")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 7: Museum Exhibition Description Generator
    elif feature.startswith("7."):
        st.header("🏛️ Museum Exhibition Description Generator")
        st.write("Create engaging, accessible descriptions for museum visitors and virtual exhibitions.")
        
        uploaded_file = st.file_uploader("Upload artwork image", type=['png', 'jpg', 'jpeg'])
        target_audience = st.selectbox("Target Audience:", 
                                      ["General Public", "Children (8-12)", "Art Students", "Scholars", "Virtual Tour Visitors"])
        tone = st.selectbox("Tone:", ["Educational", "Conversational", "Inspirational", "Technical"])
        
        if st.button("Generate Description"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Artwork", use_container_width=True)
                
                with st.spinner("Generating exhibition description..."):
                    prompt = f"""As a museum curator, create an engaging exhibition description for this artwork:
                    
                    Target Audience: {target_audience}
                    Tone: {tone}
                    
                    Include:
                    1. Captivating opening that draws viewers in
                    2. Description of what's depicted in the artwork
                    3. Historical and cultural context
                    4. Artistic techniques and significance
                    5. Emotional or intellectual impact
                    6. Questions or prompts for deeper engagement
                    7. Connection to broader themes or movements
                    
                    Make it accessible, engaging, and appropriate for the target audience. 
                    Length: 150-250 words for a wall placard or audio guide."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Description Generated!")
                        st.markdown("### 📝 Exhibition Description")
                        st.info(response.text)
                        st.download_button(
                            label="Download Description",
                            data=response.text,
                            file_name="exhibition_description.txt",
                            mime="text/plain"
                        )
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 8: Damage Pattern Recognition
    elif feature.startswith("8."):
        st.header("🔍 Damage Pattern Recognition")
        st.write("Identify patterns of damage and their potential causes.")
        
        uploaded_file = st.file_uploader("Upload artwork image showing damage", type=['png', 'jpg', 'jpeg'])
        storage_history = st.text_area("Storage/environmental history (if known):", 
                                      placeholder="E.g., stored in basement, exposed to sunlight, humid climate...")
        
        if st.button("Analyze Damage Patterns"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Artwork with Damage", use_container_width=True)
                
                with st.spinner("Analyzing damage patterns..."):
                    prompt = f"""As a conservation scientist, analyze the damage patterns in this artwork:
                    
                    1. Identify all visible types of damage (cracks, discoloration, flaking, etc.)
                    2. Determine the pattern and distribution of damage
                    3. Diagnose probable causes (age, environmental, handling, etc.)
                    4. Explain how different types of damage interact or compound
                    5. Assess whether damage is active or stable
                    6. Predict potential future deterioration if left untreated
                    7. Recommend immediate stabilization measures
                    
                    Storage/environmental context: {storage_history if storage_history else 'Unknown'}
                    
                    Provide a forensic analysis that helps understand the damage's origin and progression."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Analysis Complete!")
                        st.markdown("### 🔬 Damage Pattern Analysis")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")
    
    # Feature 9: Conservation Best Practices
    elif feature.startswith("9."):
        st.header("✅ Conservation Best Practices")
        st.write("Get expert guidance on preserving and protecting artworks.")
        
        artwork_type = st.selectbox("Artwork Type:", 
                                    ["Oil Painting", "Watercolor", "Drawing", "Sculpture (Stone)", 
                                     "Sculpture (Metal)", "Textile", "Photograph", "Mixed Media"])
        storage_location = st.selectbox("Storage/Display Location:", 
                                       ["Home", "Gallery", "Museum", "Archive", "Outdoor"])
        climate = st.selectbox("Climate:", ["Humid", "Dry", "Temperate", "Variable"])
        
        uploaded_file = st.file_uploader("Upload artwork image (optional)", type=['png', 'jpg', 'jpeg'])
        
        if st.button("Get Conservation Guide"):
            prompt = f"""As a preventive conservation expert, provide comprehensive best practices for:
            
            Artwork Type: {artwork_type}
            Location: {storage_location}
            Climate: {climate}
            
            Cover:
            1. Optimal environmental conditions (temperature, humidity, light levels)
            2. Proper handling techniques
            3. Display and storage recommendations
            4. Protection from common threats (UV light, pollution, pests, etc.)
            5. Regular maintenance and inspection schedule
            6. Emergency preparedness (fire, flood, etc.)
            7. Long-term preservation strategies
            8. When to seek professional conservation help
            
            Provide practical, implementable advice for non-experts while noting when professional intervention is needed."""
            
            with st.spinner("Generating conservation guide..."):
                try:
                    if uploaded_file:
                        image = Image.open(uploaded_file)
                        st.image(image, caption="Artwork", use_container_width=True)
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                    else:
                        response = model.generate_content(
                            prompt,
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                    st.success("Guide Generated!")
                    st.markdown("### 📋 Conservation Best Practices")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Feature 10: Virtual Restoration Preview Description
    elif feature.startswith("10."):
        st.header("🖼️ Virtual Restoration Preview Description")
        st.write("Get a detailed description of how the artwork might look after restoration.")
        
        uploaded_file = st.file_uploader("Upload current state of artwork", type=['png', 'jpg', 'jpeg'])
        restoration_goals = st.text_area("Restoration goals:", 
                                        placeholder="E.g., remove yellowed varnish, repair tears, restore faded blues...")
        
        if st.button("Generate Restoration Preview"):
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Current State", use_container_width=True)
                
                with st.spinner("Generating restoration preview description..."):
                    prompt = f"""As an expert art restorer, provide a detailed description of how this artwork will look after restoration:
                    
                    Restoration goals: {restoration_goals if restoration_goals else 'General restoration to original condition'}
                    
                    Describe:
                    1. Current state summary
                    2. Step-by-step visual transformation during restoration
                    3. Expected appearance after each major restoration phase
                    4. Final restored state - colors, clarity, details that will be revealed
                    5. Comparison between current state and expected restored appearance
                    6. What viewers will be able to see that's currently hidden or unclear
                    7. Overall visual impact of the restoration
                    
                    Paint a vivid picture with words so stakeholders can visualize the restoration outcome. 
                    Be realistic about what can and cannot be achieved."""
                    
                    try:
                        response = model.generate_content(
                            [prompt, image],
                            generation_config=genai.types.GenerationConfig(
                                temperature=temperature,
                                top_p=top_p,
                            )
                        )
                        st.success("Preview Generated!")
                        st.markdown("### 🎨 Restoration Preview Description")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please upload an image first.")

else:
    st.info("👈 Enter your Gemini API key in the sidebar to get started!")
    st.markdown("""
    ### How to get a Gemini API Key:
    1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. Sign in with your Google account
    3. Click "Get API Key"
    4. Copy your API key and paste it in the sidebar
    
    ### About ArtRestorer AI:
    This application helps museums, art historians, and conservators with:
    - Analyzing artwork condition
    - Recommending restoration techniques
    - Researching historical context
    - Interpreting symbols and inscriptions
    - And much more!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🎨 ArtRestorer AI - Preserving Cultural Heritage with AI Technology</p>
    <p>Built with Streamlit & Google Gemini 1.5 Pro</p>
</div>
""", unsafe_allow_html=True)
