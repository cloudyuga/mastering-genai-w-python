# 🔐 How to Generate a GitHub Personal Access Token (PAT)

This guide will walk you through generating a GitHub token for secure access to your repositories and GitHub API.

---

## ✅ Step-by-Step Guide

### 1. **Log In to GitHub**
Visit [https://github.com](https://github.com) and sign in to your GitHub account.

---

### 2. **Navigate to Developer Settings**
- Click your profile icon in the top-right corner.
- Select **"Settings"**.
- Scroll down the sidebar and click **"Developer settings"**.

---

### 3. **Access Personal Access Tokens**
- Click **"Personal access tokens" → "Tokens (classic)"**.
- Or choose **"Fine-grained tokens"** (recommended for more security).

---

### 4. **Generate a New Token**
- Click **“Generate new token”** and choose either:
  - **Classic** (simpler but older)
  - **Fine-grained** (more secure and recommended)

---

### 5. **Set Token Details**
Fill in the following fields:
- **Note** (a descriptive name)
- **Expiration Date**
- **Scopes (Permissions)**

**Common scopes:**
- `repo` – Full control of repositories
- `workflow` – Required for GitHub Actions
- `read:org` – To access organization data

Click **Generate token** when done.

---

### 6. **Copy the Token**
- **⚠️ Important:** Copy the token **immediately**. You won’t be able to see it again later. paste in `.env` file

---

