# 🛠️ Discord-to-HuggingFace Message Translation Pipeline

## 🔁 Flow Overview

**Discord Chat Message —> Huggingface Application —> Translate —> Back to Discord**

---

## ✅ Step 1: Create a Gradio Application

Build a translation app that translates messages from **English to Hindi**.

🔗 Live App: [Gradio App on Hugging Face](https://huggingface.co/spaces/cloudyuga/msg-translation-app/)

If you are not able to run this app, create your own space on huggingface using `translator_app.py`

---

## ✅ Step 2: Create a Discord Bot (Using `discord_file.py`)

Use the `discord_file.py` library to capture chat messages from a channel or DM.

---

## ✅ Step 3: Generate Discord Bot Token

### 🧩 Step-by-Step: Get Your Discord Bot Token

1. Go to the Discord Developer Portal  
   👉 https://discord.com/developers/applications

2. Click **"New Application"**  
   - Give it a name (e.g., `demo-app`)  
   - Click **Create**

3. Create a Bot  
   - In the left menu, click **"Bot"**  
   - Click **"Add Bot"** → Confirm with **Yes, do it!**

4. Reveal the Token  
   - Under **Bot** section, locate **Token**  
   - Click **"Reset Token"** (if needed) → **Copy** it  
   ⚠️ **Never share this token publicly**  
   - Save it in a `.env` file or as an environment variable

---

## ✅ Step 4: Enable Privileged Intents

1. In the left sidebar, go to **Bot**  
2. Scroll down to **Privileged Gateway Intents**

Enable the following:
- ✅ Message Content Intent  
- ✅ Presence Intent *(optional)*  
- ✅ Server Members Intent *(optional)*

Click **Save Changes**

---

## ✅ Step 5: Invite Bot to Your Server

1. Navigate to **OAuth2 > URL Generator**
2. Under **Scopes**, check:
   - `bot`
3. Under **Bot Permissions**, select:
   - ✅ Read Messages  
   - ✅ Send Messages  
   *(Optionally: View Channels, Embed Links, etc.)*

4. Copy the generated URL and open it in your browser  
5. Authorize the bot to join your server

---

## ✅ Step 6: Authorize Bot Access to Server

1. Select your Discord server (you must be an **Admin**)  
2. Click **Continue → Authorize**  
3. Complete the CAPTCHA if prompted

### ❗ If Your Server Doesn’t Show Up:
- You are likely **not an admin** on the server

#### Fix:
- Ask the server admin to:
  - Grant you the **Administrator** role  
  - **OR** open the OAuth2 URL and authorize the bot themselves

---

## ✅ Step 7: Add a New Server to Your Discord Account

1. Click **Add a Server** in Discord  
2. Choose **Create My Own**  
3. Name your server  
4. Click **Create**

Now return to **Step 6** — your new server should now be available to select.

---

## ✅ Step 8: Run the App

- Open the CY-Server (your Discord server)
- You’ll see a message like:  
  `"Good to see you, demo-app. 2:33 PM"`

- Type a message in English  
- Your `demo-app` will translate the message to **Hindi**

---

🧩 Enjoy real-time translation from Discord to HuggingFace and back!
