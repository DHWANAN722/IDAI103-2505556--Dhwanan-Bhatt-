# 📝 ArtRestorer AI - Prompt Documentation

## Overview of All 10 AI Features

This document provides detailed information about each of the 10 AI-powered features in ArtRestorer AI, including prompt design, use cases, and expected outputs.

---

## Feature 1: Artwork Analysis & Condition Assessment

### Purpose
Provides comprehensive condition assessments for artworks by analyzing visual damage, deterioration, and overall state.

### Prompt Design
```
As an expert art conservator, analyze this artwork image and provide a detailed condition assessment including:
1. Overall condition rating (Excellent/Good/Fair/Poor)
2. Visible damage or deterioration (cracks, discoloration, fading, etc.)
3. Areas of concern that need immediate attention
4. Estimated age and condition based on visual analysis
5. Urgency level for restoration (Low/Medium/High/Critical)

Additional context: [User-provided details]

Provide your analysis in a professional, structured format.
```

### Input Parameters
- **Image**: Artwork photograph
- **Text**: Optional description of artwork history
- **Temperature**: 0.7 (balanced for accuracy and detail)
- **Top P**: 0.9

### Expected Output
A structured report containing:
- Overall condition rating
- Detailed damage inventory
- Priority areas for attention
- Restoration urgency assessment

### Use Cases
- Museum intake assessments
- Insurance documentation
- Pre-restoration evaluation
- Collection management

---

## Feature 2: Restoration Technique Recommendations

### Purpose
Provides step-by-step restoration guidance based on artwork type and specific damage patterns.

### Prompt Design
```
As a master art restorer, provide detailed restoration technique recommendations for:

Artwork Type: [Oil Painting/Watercolor/Fresco/etc.]
Damage Observed: [Cracks/Fading/Water Damage/etc.]
Approximate Age: [Time period]

Please provide:
1. Step-by-step restoration approach
2. Recommended materials and tools
3. Precautions and risks to be aware of
4. Estimated timeframe for restoration
5. Whether professional intervention is required
6. Alternative techniques if traditional methods are too risky

Be specific, practical, and culturally sensitive to the artwork's heritage.
```

### Input Parameters
- **Artwork Type**: Dropdown selection
- **Damage Type**: Multi-select checkboxes
- **Age**: Text input
- **Image**: Optional
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Detailed step-by-step restoration plan
- Materials and tools list
- Risk assessment
- Timeline estimation
- Professional vs. DIY guidance

### Use Cases
- Planning restoration projects
- Training restoration students
- Evaluating restoration options
- Cost estimation preparation

---

## Feature 3: Historical Context & Provenance Research

### Purpose
Analyzes artworks to determine likely historical period, artistic movement, cultural origin, and significance.

### Prompt Design
```
As an art historian, analyze this artwork and provide insights about:

1. Possible time period and artistic movement (Renaissance, Baroque, Impressionism, etc.)
2. Regional/cultural origin indicators (style, technique, subject matter)
3. Similar known works or artists with comparable styles
4. Historical context of the depicted subject or scene
5. Potential significance in art history
6. Suggestions for further provenance research

Known information: [User input]

Provide an educational, engaging analysis that helps understand the artwork's place in history.
```

### Input Parameters
- **Image**: Artwork photograph
- **Known Info**: Text area for existing knowledge
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Time period identification
- Artistic movement analysis
- Cultural origin indicators
- Comparative analysis with known works
- Research recommendations

### Use Cases
- Estate sales and acquisitions
- Museum cataloging
- Academic research
- Authenticating artworks
- Exhibition planning

---

## Feature 4: Symbol & Inscription Interpretation

### Purpose
Decodes symbols, inscriptions, signatures, and text found in artworks across various languages and symbolic systems.

### Prompt Design
```
As an expert in art history, iconography, and ancient languages, analyze the symbols and inscriptions in this image:

1. Identify any visible text, symbols, or markings
2. Determine the likely language or symbolic system
3. Provide translation or interpretation where possible
4. Explain cultural or religious significance
5. Date the inscription style if possible
6. Suggest what the symbols might reveal about the artwork's origin or purpose

Context: [User-provided context]

Be scholarly but accessible in your explanation.
```

### Input Parameters
- **Image**: Close-up of symbols/inscriptions
- **Context**: Text area for additional information
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Text transcription
- Translation (if possible)
- Symbol identification
- Cultural significance explanation
- Dating information
- Origin insights

### Use Cases
- Decoding artist signatures
- Interpreting religious symbols
- Translating inscriptions
- Understanding iconography
- Provenance research

---

## Feature 5: Material Composition Analysis

### Purpose
Identifies materials, techniques, and mediums used in creating the artwork.

### Prompt Design
```
As a materials science expert specializing in art conservation, analyze this artwork and provide insights about:

1. Likely painting medium (oil, acrylic, tempera, watercolor, etc.)
2. Canvas or support material characteristics
3. Pigments that may have been used (based on colors and time period)
4. Special materials detected (gold leaf, varnish, etc.)
5. Application techniques visible (impasto, glazing, etc.)
6. How materials may have degraded over time
7. Conservation implications based on materials

Additional details: [User input]

Explain in a way that helps with restoration planning.
```

### Input Parameters
- **Image**: Artwork photograph
- **Details**: Text area for known information
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Medium identification
- Support material analysis
- Pigment speculation
- Technique description
- Degradation assessment
- Conservation recommendations

### Use Cases
- Restoration planning
- Authentication verification
- Conservation strategy development
- Educational purposes
- Collection documentation

---

## Feature 6: Color Palette Restoration Guidance

### Purpose
Provides color matching recommendations and guidance for restoring original color palettes.

### Prompt Design
```
As a color specialist and art restorer, analyze this artwork's color palette and provide:

1. Current dominant colors and their condition
2. Identification of faded or altered colors
3. Likely original color palette based on visible remnants and artistic period
4. Specific pigment recommendations for color matching
5. Color mixing ratios and techniques
6. How to achieve color consistency across restored areas
7. Testing recommendations before full application

Fading information: [User description]

Provide practical, actionable color restoration guidance.
```

### Input Parameters
- **Image**: Artwork with color issues
- **Fading Areas**: Description of color problems
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Current color analysis
- Original palette reconstruction
- Pigment recommendations
- Mixing instructions
- Testing protocols
- Application guidance

### Use Cases
- Color restoration projects
- Touch-up work
- Varnish removal planning
- Matching historical pigments
- Training restoration students

---

## Feature 7: Museum Exhibition Description Generator

### Purpose
Creates engaging, accessible descriptions for museum wall placards, audio guides, and virtual exhibitions.

### Prompt Design
```
As a museum curator, create an engaging exhibition description for this artwork:

Target Audience: [General Public/Children/Students/Scholars/Virtual Visitors]
Tone: [Educational/Conversational/Inspirational/Technical]

Include:
1. Captivating opening that draws viewers in
2. Description of what's depicted in the artwork
3. Historical and cultural context
4. Artistic techniques and significance
5. Emotional or intellectual impact
6. Questions or prompts for deeper engagement
7. Connection to broader themes or movements

Make it accessible, engaging, and appropriate for the target audience.
Length: 150-250 words for a wall placard or audio guide.
```

### Input Parameters
- **Image**: Artwork
- **Target Audience**: Dropdown selection
- **Tone**: Dropdown selection
- **Temperature**: 0.8 (more creative for engaging writing)
- **Top P**: 0.9

### Expected Output
- Engaging 150-250 word description
- Audience-appropriate language
- Educational content
- Emotional connection points
- Downloadable text file

### Use Cases
- Museum exhibitions
- Virtual tours
- Educational materials
- Audio guide scripts
- Marketing materials

---

## Feature 8: Damage Pattern Recognition

### Purpose
Identifies damage patterns, diagnoses causes, and predicts future deterioration.

### Prompt Design
```
As a conservation scientist, analyze the damage patterns in this artwork:

1. Identify all visible types of damage (cracks, discoloration, flaking, etc.)
2. Determine the pattern and distribution of damage
3. Diagnose probable causes (age, environmental, handling, etc.)
4. Explain how different types of damage interact or compound
5. Assess whether damage is active or stable
6. Predict potential future deterioration if left untreated
7. Recommend immediate stabilization measures

Storage/environmental context: [User input]

Provide a forensic analysis that helps understand the damage's origin and progression.
```

### Input Parameters
- **Image**: Damaged artwork
- **Storage History**: Environmental context
- **Temperature**: 0.7
- **Top P**: 0.9

### Expected Output
- Damage inventory
- Pattern analysis
- Cause diagnosis
- Stability assessment
- Future risk prediction
- Stabilization recommendations

### Use Cases
- Damage assessment
- Insurance claims
- Prevention planning
- Emergency conservation
- Educational training

---

## Feature 9: Conservation Best Practices

### Purpose
Provides comprehensive guidance on proper storage, handling, and preservation of artworks.

### Prompt Design
```
As a preventive conservation expert, provide comprehensive best practices for:

Artwork Type: [Oil Painting/Watercolor/Sculpture/etc.]
Location: [Home/Gallery/Museum/Archive/Outdoor]
Climate: [Humid/Dry/Temperate/Variable]

Cover:
1. Optimal environmental conditions (temperature, humidity, light levels)
2. Proper handling techniques
3. Display and storage recommendations
4. Protection from common threats (UV light, pollution, pests, etc.)
5. Regular maintenance and inspection schedule
6. Emergency preparedness (fire, flood, etc.)
7. Long-term preservation strategies
8. When to seek professional conservation help

Provide practical, implementable advice for non-experts while noting when professional intervention is needed.
```

### Input Parameters
- **Artwork Type**: Dropdown
- **Location**: Dropdown
- **Climate**: Dropdown
- **Image**: Optional
- **Temperature**: 0.6 (more factual, less creative)
- **Top P**: 0.9

### Expected Output
- Environmental guidelines
- Handling instructions
- Storage recommendations
- Protection strategies
- Maintenance schedule
- Emergency procedures
- Professional consultation indicators

### Use Cases
- Private collections
- Gallery management
- Museum standards
- Archive preservation
- Educational purposes

---

## Feature 10: Virtual Restoration Preview Description

### Purpose
Creates vivid written descriptions of expected restoration outcomes, helping stakeholders visualize results.

### Prompt Design
```
As an expert art restorer, provide a detailed description of how this artwork will look after restoration:

Restoration goals: [User-specified goals]

Describe:
1. Current state summary
2. Step-by-step visual transformation during restoration
3. Expected appearance after each major restoration phase
4. Final restored state - colors, clarity, details that will be revealed
5. Comparison between current state and expected restored appearance
6. What viewers will be able to see that's currently hidden or unclear
7. Overall visual impact of the restoration

Paint a vivid picture with words so stakeholders can visualize the restoration outcome.
Be realistic about what can and cannot be achieved.
```

### Input Parameters
- **Image**: Current artwork state
- **Restoration Goals**: Text area
- **Temperature**: 0.8 (creative for vivid descriptions)
- **Top P**: 0.9

### Expected Output
- Current state description
- Phase-by-phase transformation narrative
- Final appearance visualization
- Before/after comparison
- Realistic expectations
- Impact assessment

### Use Cases
- Restoration proposals
- Fundraising presentations
- Client communications
- Project planning
- Educational demonstrations

---

## Model Parameter Guidelines

### Temperature Settings
- **0.3-0.5**: Technical, factual features (Material Analysis, Best Practices)
- **0.6-0.7**: Balanced features (most assessment and analysis tasks)
- **0.8-1.0**: Creative features (Exhibition Descriptions, Preview Descriptions)

### Top P Settings
- **0.8-0.9**: Standard for most features (good balance)
- **0.9-1.0**: For diverse, creative outputs

### Optimization Notes
- Features tested with multiple parameter combinations
- Error handling implemented for API failures
- Image size optimization for faster processing
- User feedback incorporated for prompt refinement

---

## Prompt Engineering Techniques Used

1. **Role Assignment**: Each prompt assigns AI a specific expert role
2. **Structured Output**: Numbered lists ensure comprehensive responses
3. **Context Integration**: User inputs seamlessly incorporated
4. **Audience Awareness**: Prompts consider end-user needs
5. **Cultural Sensitivity**: Emphasis on respectful heritage treatment
6. **Practical Focus**: Actionable, implementable guidance
7. **Clarity**: Clear, specific instructions for consistent results
8. **Flexibility**: Handles varying levels of user-provided information
9. **Education**: Balances expert knowledge with accessibility
10. **Safety**: Reminds users when professional help is needed

---

## Testing & Validation

Each feature has been tested with:
- ✅ Multiple image types (paintings, sculptures, documents)
- ✅ Various damage conditions
- ✅ Different artistic periods and styles
- ✅ Edge cases (unclear images, minimal context)
- ✅ Different parameter settings
- ✅ Error scenarios (no image, API failures)

## Future Enhancements

Potential improvements for future versions:
- Multi-language support
- Batch processing for multiple artworks
- PDF report generation
- Integration with museum databases
- Collaborative features for teams
- Advanced image processing filters
- Historical artwork database search

---

**Documentation Version**: 1.0  
**Last Updated**: February 2026  
**Course**: Year 1 - Generative AI  
**Assessment**: Summative Assignment
