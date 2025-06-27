# 📥 How to Download and Run Gmail Inbox Tool

## 1. Go to Google Cloud Console
👉 https://console.cloud.google.com/

- Log in with your Google account.
- Create a new project (or select an existing one).

---

## 2. Enable Gmail API

- In the Cloud Console, go to:  
  `APIs & Services` > `Library`
- Search for **Gmail API**
- Click **Enable**

---

## 🛠 3. Create OAuth 2.0 Client Credentials

- Navigate to: `APIs & Services` > `Credentials`
- Click **+ CREATE CREDENTIALS** → choose **OAuth client ID**

### If you haven't configured the OAuth consent screen:
- Click **Get Started**
- **App name**: e.g., `Gmail-Inbox-App`
- **User type / Audience**: `External`
- **Test users**: Add your Gmail address

### Then:
- Click **Create OAuth client ID**
- **Application type**: `Desktop app`
- **Name**: `Gmail-Inbox-Tool` (or any name you prefer)
- **Create**

---

## 📁 4. Download `credentials.json`

- After creating the OAuth client, click the download button 📥 next to it.
- Save the file and optionally rename it as `credentials.json`

---

# ▶️ How to Run the Application

Install required Python packages:
```bash
pip install -r requirements.txt
```

Then run the Gradio App:
```bash
python gradio_gmail_chat.py
```
### For the first time run gradio_gmail_chat.py,

You will see a URL like this in the terminal:
```
Please visit this URL to authorize this application: https://accounts.google.com
```

Allow access to:
- View your email messages and settings

Once completed, you'll see:
```
The authentication flow has completed. You may close this window.
```
Get back to the Gradio UI for QA with Gmail Account
