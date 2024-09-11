
## Development

### Setting up the environment

1. **Set up the GitHub OAuth application** (if not already done).
2. **Set up the Telegram bot** (if not already done).
3. **Set up the Google Cloud project** (if not already done).
4. **Set up the Google Sheets API** (if not already done).
5. **Set up the service account** (if not already done).
6. **Set up the environment variables** (if not already done).
7. **Install pre-commit hooks**. (if not already done).
8. **Run the application**.

### Step 1: Set Up GitHub OAuth Application

If you haven’t already created a GitHub OAuth app, follow these steps:

- Go to [GitHub Developer Settings](https://github.com/settings/developers).
- Under **OAuth Apps**, click **New OAuth App**.
- Fill in the details:
  - **Application name**: Your app’s name.
  - **Homepage URL**: The URL of your web page (e.g., `http://localhost:5000` for local development).
  - **Authorization callback URL**: The URL where GitHub will redirect users after they authorize your app (e.g., `http://localhost:5000/callback`).

After creating the app, you’ll receive a **Client ID** and **Client Secret**.

### Step 2: Set Up Telegram Bot

- Go to [BotFather](https://t.me/botfather) and create a new bot.
- You will receive a token for your bot.

### Step 4: Set Up Google Cloud Project

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the **Google Sheets API** for your project.

### Step 5: Set Up Service Account

- Go to the [Google Cloud Console **IAM & Admin** > **Service Accounts*](https://console.cloud.google.com/iam-admin/serviceaccounts).
- Create a new service account or select an existing one.
- Go to the **Keys** tab and create a new key.
- Download the JSON key file and save it in the openhopehack folder in the project.
- Rename the file to `sa-<project-id>.json`.
- Open the file and copy the `client_email` field.
- Add the `client_email` to the desired google sheet as an editor.

### Step 6: Set Up Environment Variables

- Set the following environment variables in your `.env` file:

```
LOG_LEVEL=DEBUG
GITHUB_CLIENT_ID=<your-github-client-id>
GITHUB_CLIENT_SECRET=<your-github-client-secret>
GDRIVE_CREDENTIALS=<your-service-account-key-file-name>
OAUTHLIB_INSECURE_TRANSPORT=1
GOOGLE_SPREADSHEET_ID = <your-google-spreadsheet-id>
TELEGRAM_TOKEN = <your-telegram-token>
TELEGRAM_CHAT_ID = <your-telegram-chat-id>
```

### Step 7: Install pre-commit hooks

Install pre-commit
```
pip install pre-commit
```

Install pre-commit hooks
```
pre-commit install
```

### Step 8: Run the Application

```
make setup-venv
make run
```
