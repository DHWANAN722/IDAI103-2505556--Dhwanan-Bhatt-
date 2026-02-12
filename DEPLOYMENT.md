# 🚀 Deployment Guide - ArtRestorer AI

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [GitHub Setup](#github-setup)
3. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
4. [Testing Your Deployed App](#testing-your-deployed-app)
5. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before deploying, ensure you have:
- ✅ A GitHub account ([Sign up here](https://github.com/join))
- ✅ Git installed on your computer ([Download here](https://git-scm.com/downloads))
- ✅ All project files (app.py, requirements.txt, README.md, etc.)
- ✅ A Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

---

## GitHub Setup

### Step 1: Create a New Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `artrestorer-ai` (or your preferred name)
   - **Description**: "AI-Powered Art Restoration Assistant using Gemini 1.5 Pro"
   - **Visibility**: Public (required for free Streamlit Cloud)
   - **Initialize**: Don't check any boxes (we have our own files)
5. Click **"Create repository"**

### Step 2: Upload Your Code to GitHub

#### Option A: Using Git Command Line (Recommended)

1. Open Terminal/Command Prompt
2. Navigate to your project folder:
```bash
cd path/to/your/artrestorer-ai
```

3. Initialize Git (if not already done):
```bash
git init
```

4. Add all files:
```bash
git add .
```

5. Commit your files:
```bash
git commit -m "Initial commit - ArtRestorer AI application"
```

6. Link to your GitHub repository (replace YOUR_USERNAME):
```bash
git remote add origin https://github.com/YOUR_USERNAME/artrestorer-ai.git
```

7. Push to GitHub:
```bash
git branch -M main
git push -u origin main
```

#### Option B: Using GitHub Website (Easier for beginners)

1. Go to your new repository on GitHub
2. Click **"uploading an existing file"**
3. Drag and drop all your project files:
   - app.py
   - requirements.txt
   - README.md
   - .gitignore
   - docs/ folder
4. Click **"Commit changes"**

---

## Streamlit Cloud Deployment

### Step 1: Sign Up for Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **"Sign up"** or **"Get started"**
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your GitHub account

### Step 2: Deploy Your App

1. Once logged in, click **"New app"** (or **"Create app"**)

2. Fill in the deployment settings:
   - **Repository**: Select `yourusername/artrestorer-ai`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: Choose a custom name (e.g., `artrestorer-ai`) or use auto-generated

3. Click **"Deploy!"**

4. Wait for deployment (usually 2-5 minutes)
   - You'll see build logs showing installation progress
   - Green checkmark = Successfully deployed!

### Step 3: Save Your App URL

Once deployed, you'll get a URL like:
```
https://artrestorer-ai-yourname.streamlit.app
```

**Copy this URL** - you'll need it for your assignment submission!

---

## Testing Your Deployed App

### Step 1: Access Your App
1. Open your app URL in a browser
2. You should see the ArtRestorer AI interface

### Step 2: Test Basic Functionality
1. **Enter API Key**: Paste your Gemini API key in the sidebar
2. **Select a Feature**: Choose "1. Artwork Analysis & Condition Assessment"
3. **Upload an Image**: Use any artwork image (you can find free images on [Unsplash](https://unsplash.com/s/photos/painting))
4. **Test the AI**: Click "Analyze Artwork" and verify you get a response

### Step 3: Test Multiple Features
- Try at least 3 different features to ensure they all work
- Test with and without images
- Adjust temperature/top_p settings to see different outputs

### Step 4: Check Mobile Responsiveness
- Open your app URL on a mobile device
- Verify the interface is usable on smaller screens

---

## Troubleshooting

### Common Issues and Solutions

#### 1. **App Won't Deploy / Build Fails**

**Error**: `ModuleNotFoundError` or package installation fails

**Solution**:
- Check your `requirements.txt` for typos
- Make sure versions are compatible
- Try these tested versions:
```
streamlit==1.31.0
google-generativeai==0.3.2
Pillow==10.2.0
```

#### 2. **API Key Not Working**

**Error**: `API key not valid` or authentication errors

**Solution**:
- Get a fresh API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Make sure you're using Gemini 1.5 Pro (not older models)
- Check for extra spaces when pasting the key

#### 3. **Images Not Uploading**

**Error**: Upload fails or images don't display

**Solution**:
- Use JPG or PNG format only
- Keep file size under 10MB
- Try a different browser if issues persist

#### 4. **Slow Response Times**

**Issue**: AI takes too long to respond

**Solution**:
- This is normal - Gemini can take 5-30 seconds for complex analysis
- Reduce image size if very large
- Check your internet connection

#### 5. **App Shows "Sleeping" or "Inactive"**

**Issue**: Streamlit Cloud apps sleep after inactivity

**Solution**:
- This is normal for free tier
- App will wake up when accessed (takes ~10 seconds)
- Consider upgrading for 24/7 availability if needed

#### 6. **Changes Not Showing After Git Push**

**Issue**: Updated code but app still shows old version

**Solution**:
1. Go to your Streamlit Cloud dashboard
2. Find your app
3. Click **"Reboot app"** or the three dots menu → **"Reboot"**
4. Wait for rebuild

---

## Updating Your Deployed App

### When You Make Changes to Code:

1. **Edit your files locally**

2. **Commit and push changes**:
```bash
git add .
git commit -m "Description of changes"
git push
```

3. **Streamlit Cloud will automatically redeploy** (usually within 1-2 minutes)

---

## Performance Optimization Tips

### 1. Image Optimization
```python
# Add this to resize large images before sending to API
if uploaded_file:
    image = Image.open(uploaded_file)
    # Resize if too large
    if image.width > 1024 or image.height > 1024:
        image.thumbnail((1024, 1024))
```

### 2. Caching
```python
# Add caching for repeated API calls
@st.cache_data
def analyze_artwork(image, prompt):
    # Your API call here
    pass
```

### 3. Error Handling
Already implemented in the app:
```python
try:
    response = model.generate_content(...)
except Exception as e:
    st.error(f"Error: {str(e)}")
```

---

## Security Best Practices

### ⚠️ IMPORTANT: Never commit API keys to GitHub!

✅ **Correct Way**: User enters API key in the app interface
❌ **Wrong Way**: Hardcoding API key in app.py

### Additional Security Tips:
1. Keep `.gitignore` file to exclude sensitive files
2. Don't commit `.env` files
3. Use Streamlit secrets for production (see [docs](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management))

---

## Resources

### Official Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [GitHub Guides](https://guides.github.com/)

### Support
- [Streamlit Community Forum](https://discuss.streamlit.io/)
- [GitHub Help](https://docs.github.com/)

---

## Checklist Before Submission

Use this checklist to ensure everything is ready:

- [ ] All code files uploaded to GitHub
- [ ] README.md is complete with your information
- [ ] App deployed successfully on Streamlit Cloud
- [ ] App URL is accessible and working
- [ ] Tested all 10 features with sample inputs
- [ ] API key entry works correctly
- [ ] No errors in the deployed version
- [ ] Mobile responsiveness verified
- [ ] GitHub repository is public
- [ ] Repository has a good description
- [ ] Documentation (docs/prompts.md) is included

---

## Final Steps for Assignment Submission

1. **Copy your deployed app URL**
2. **Add it to your README.md** under "Live Demo"
3. **Take screenshots** of:
   - Your GitHub repository
   - Your deployed app homepage
   - At least 3 features in action
4. **Document your testing** in the README
5. **Submit your GitHub repository link** as required by your instructor

---

**Good luck with your deployment! 🚀**

If you encounter any issues not covered here, feel free to search the Streamlit Community Forum or GitHub Issues for solutions.
