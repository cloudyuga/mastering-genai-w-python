# How to download 
## 1. Go to Google Cloud Console

https://console.cloud.google.com/

Log in with your Google account.

Create a new project (or select an existing one).

## 2. Enable Gmail API
In the Cloud Console, go to:

"APIs & Services" > "Library"

Search for Gmail API

Click "Enable"

## 🛠 3. Create OAuth 2.0 Client Credentials
Go to: APIs & Services > Credentials

Click “+ CREATE CREDENTIALS” → choose OAuth client ID

Configure OAuth consent screen (if not done yet):

get strated

App name: e.g., Gmail-Inbox-App

User type/ Audience: External

Add your Gmail address as a test user

After configuring, click:

Create OAuth client ID

choose,

Application type: Desktop app

Name: Gmail-Inbox-Tool (or anything)

## 📁 4. Download credentials.json
After creating the OAuth client, click the download button (📥) next to it.

This is your credentials.json file. Rename it.

# How to run the application

```
pip install -r requirements.txt
```
Run Gradio App
```
gradio_gmail_chat.py
```

Please visit this URL to authorize this application: https://accounts.google.com from the terminal and allow 

View your email messages and settings

The authentication flow has completed. You may close this window.
