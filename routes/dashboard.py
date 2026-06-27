from flask import Blueprint,render_template,session,redirect,url_for
from database.database import get_db_connection
dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def home():
    return redirect(
        url_for("dashboard.dashboard_page")
    )

@dashboard.route("/dashboard")
def dashboard_page():
    # Authentication
    if "user_id" not in session:
        return redirect(
            url_for("auth.login")
        )

    # Load Analysis History
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            jd.job_role,
            ar.ats_score,
            ar.similarity_score,
            ar.analyzed_at
        FROM analysis_results ar
        JOIN job_descriptions jd
            ON ar.job_description_id = jd.id
        WHERE ar.user_id=?
        ORDER BY ar.analyzed_at DESC
        LIMIT 5
        """,
        (session["user_id"],)
    )
    history = cursor.fetchall()
    conn.close()

    # Render Dashboard
    return render_template(
        "dashboard.html",
        analysis=None,
        history=history,
        chart_data={},
        history_chart=[]
    )