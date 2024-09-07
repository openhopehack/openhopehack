from flask import Blueprint, render_template

base_bp = Blueprint(
    "base", __name__, template_folder="templates", static_folder="static"
)


@base_bp.route("/")
def index():
    return render_template("index.html")
