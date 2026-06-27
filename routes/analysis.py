from flask import Blueprint,request,render_template,redirect,url_for,session,flash
import os
from werkzeug.utils import secure_filename

from database.database import get_db_connection
from database.save_analysis import save_analysis

from services.pdf_parser import extract_resume_text
from services.gemini_service import extract_resume_information,analyze_resume
from services.similarity import calculate_similarity
from services.ats_service import calculate_ats_score

analysis = Blueprint("analysis", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@analysis.route("/analyze", methods=["POST"])
def analyze():

    # Authentication
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # Get Form Data
    resume = request.files.get("resume")
    job_description = request.form.get(
        "job_description",
        ""
    ).strip()

    # Validation
    if not resume:
        flash("Please upload your resume.", "warning")
        return redirect(url_for("dashboard.dashboard_page"))

    if resume.filename == "":
        flash("Please select a PDF file.", "warning")
        return redirect(url_for("dashboard.dashboard_page"))

    if not resume.filename.lower().endswith(".pdf"):
        flash("Only PDF files are allowed.", "danger")
        return redirect(url_for("dashboard.dashboard_page"))

    if not job_description:
        flash("Please enter a Job Description.", "warning")
        return redirect(url_for("dashboard.dashboard_page"))

    try:

        # Save Uploaded Resume
        filename = secure_filename(resume.filename)
        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )
        resume.save(filepath)

        # Extract Resume Text
        resume_text = extract_resume_text(filepath)

        if not resume_text.strip():
            flash("Unable to extract text from PDF.", "danger")
            return redirect(url_for("dashboard.dashboard_page"))

        # Gemini Resume Parsing
        resume_data = extract_resume_information(
            resume_text
        )

        # Gemini Resume Analysis
        analysis_data = analyze_resume(
            resume_data,
            job_description
        )

        # Similarity Score
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ATS Score
        ats_result = calculate_ats_score(
            similarity_score,
            resume_data,
            analysis_data
        )

        # Save Analysis
        save_analysis(
            user_id=session["user_id"],
            resume_filename=filename,
            resume_filepath=filepath,
            resume_text=resume_text,
            resume_data=resume_data,
            job_description=job_description,
            analysis_data=analysis_data,
            similarity_score=similarity_score,
            ats_result=ats_result
        )

        # Dashboard Result
        analysis_result = {
            "ats_score":
                ats_result["ats_score"],
            "similarity_score":
                similarity_score,
            "matched_skills":
                analysis_data.get(
                    "matched_skills",
                    []
                ),
            "missing_skills":
                analysis_data.get(
                    "missing_required_skills",
                    analysis_data.get(
                        "missing_skills",
                        []
                    )
                ),
            "strengths":
                analysis_data.get(
                    "strengths",
                    []
                ),
            "weaknesses":
                analysis_data.get(
                    "weaknesses",
                    []
                ),
            "recommendations":
                analysis_data.get(
                    "recommendations",
                    []
                ),
            "overall_summary":
                analysis_data.get(
                    "overall_summary",
                    ""
                ),
            "breakdown":
                ats_result.get(
                    "breakdown",
                    {}
                )
        }

        # Load Previous Analysis History
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

        # Prepare Chart Data
        chart_data = {
            "ats":
                ats_result["ats_score"],
            "matched":
                len(
                    analysis_result["matched_skills"]
                ),
            "missing":
                len(
                    analysis_result["missing_skills"]
                ),
            "breakdown":
                ats_result["breakdown"]
        }
        history_chart = []
        for row in history:
            history_chart.append({
                "job":
                    row["job_role"],
                "score":
                    row["ats_score"],
                "similarity":
                    row["similarity_score"],
                "date":
                    row["analyzed_at"]
            })
        conn.close()

        # Render Dashboard
        return render_template(
            "dashboard.html",
            analysis=analysis_result,
            history=history,
            chart_data=chart_data,
            history_chart=history_chart
        )

    except Exception as e:
        print("Resume Analysis Error :", e)
        flash("Resume analysis failed. Please try again.","danger")
        return redirect(url_for("dashboard.dashboard_page"))