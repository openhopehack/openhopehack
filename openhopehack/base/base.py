from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request
from flask import current_app as app
from flask_dance.contrib.github import github
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
    login_required,
)

from .libs.telegram import Telegram

base_bp = Blueprint(
    "base", __name__, template_folder="templates", static_folder="static"
)


class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username


users = {}

# Flask-Login setup
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


@base_bp.route("/")
def index():
    return render_template("index.html")


@base_bp.route("/test")
@login_required
def test():
    return current_user.username


@base_bp.route("/submit-pr", methods=["POST"])
@login_required
def submit_pr():
    pr_url = request.form.get("pr_url")
    if not pr_url:
        return redirect(url_for("index"))

    github_username = current_user.username
    timestamp = datetime.now().isoformat()

    message = f"New PR Submission\n\nGitHub Username: {github_username}\nPR URL: {pr_url}\nTimestamp: {timestamp}"
    # Send message to Telegram group
    telegram = Telegram(app.config["TELEGRAM_BOT_TOKEN"], app.logger)
    if telegram.send_message(app.config["TELEGRAM_CHAT_ID"], message):
        return redirect(url_for("base.index"))
    else:
        return "Failed to send message to Telegram"


@base_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("base.index"))


@base_bp.route("/login")
def github_login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    if resp.ok:
        github_info = resp.json()
        username = github_info["login"]
        user_id = str(github_info["id"])
        if user_id not in users:
            users[user_id] = User(user_id, username)
        login_user(users[user_id])
    else:
        print("Error: ", resp.text)
    return redirect(url_for("base.index"))
