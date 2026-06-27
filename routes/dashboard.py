from flask import Blueprint, render_template, session, redirect, url_for
from database.database import get_db_connection

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def home():
    return redirect(url_for("dashboard.dashboard_page"))

@dashboard.route("/dashboard")
def dashboard_page():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            job_title,
            ats_score,
            similarity_score,
            created_at
        FROM analysis_history
        WHERE user_id=?
        ORDER BY created_at DESC
        LIMIT 5
    """, (session["user_id"],))
    history = cursor.fetchall()
    conn.close()
    return render_template(
        "dashboard.html",
        history=history,
        analysis=None
    )