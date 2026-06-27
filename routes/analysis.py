from flask import Blueprint,request,render_template,redirect,url_for,session,flash
from database.database import get_db_connection
from services.pdf_parser import extract_resume_text
from services.gemini_service import extract_resume_information,analyze_resume
from services.similarity import calculate_similarity
from services.ats_service import calculate_ats_score
analysis = Blueprint("analysis", __name__)

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

    # Step 1 : Extract Resume Text
    resume_text = extract_resume_text(resume)
    if not resume_text.strip():
        flash("Unable to read PDF.", "danger")
        return redirect(url_for("dashboard.dashboard_page"))

    # Step 2 : Gemini Resume Extraction
    resume_data = extract_resume_information(resume_text)

    # Step 3 : Gemini Resume Analysis
    analysis_data = analyze_resume(resume_data,job_description)
    
    # Step 4 : Similarity Score
    similarity_score = calculate_similarity(resume_text,job_description)

    # Step 5 : ATS Score
    ats_result = calculate_ats_score(similarity_score,resume_data,analysis_data)

    # Dashboard Result
    analysis_result = {
        "ats_score":
            ats_result["ats_score"],

        "similarity_score":
            similarity_score,

        "matched_skills":
            analysis_data.get("matched_skills",[]),

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
            ats_result["breakdown"]

    }

    
    # Load Previous History
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            job_title,
            ats_score,
            similarity_score,
            created_at
        FROM analysis_history
        WHERE user_id=?
        ORDER BY created_at DESC
        LIMIT 5
        """,
        (session["user_id"],)
    )

    history = cursor.fetchall()
    conn.close()

    # Render Dashboard
    return render_template(
        "dashboard.html",
        analysis=analysis_result,
        history=history
    )