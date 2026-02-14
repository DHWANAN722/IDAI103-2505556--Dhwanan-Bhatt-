# ArtRestorer AI - Setup Instructions

## 🔑 Setting Up Your OpenAI API Key

### Option 1: Local Development

1. Create a folder named `.streamlit` in your project directory
2. Inside `.streamlit`, create a file named `secrets.toml`
3. Add your API key:

```toml
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"
```

Your folder structure should look like:
```
your-project/
├── artrestorer_redesigned.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml
```

### Option 2: Streamlit Cloud Deployment

1. Go to your app on Streamlit Cloud
2. Click on **⚙️ Settings** (top right)
3. Select **Secrets** from the menu
4. Add your secret in this format:

```toml
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"
```

5. Click **Save**

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Running the App

```bash
streamlit run artrestorer_redesigned.py
```

## ⚠️ Important Security Notes

- **NEVER** commit `.streamlit/secrets.toml` to GitHub
- Add `.streamlit/` to your `.gitignore` file
- Keep your API key private and secure

## 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub (without secrets.toml)
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Connect your GitHub repository
5. Add secrets through the Streamlit Cloud interface
6. Deploy!

---

**Need help?** Check the official docs:
- Streamlit Secrets: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management
- OpenAI API: https://platform.openai.com/api-keys
