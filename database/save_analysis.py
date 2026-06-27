import json
from database.database import get_db_connection

def save_analysis(
    user_id,
    resume_filename,
    resume_filepath,
    resume_text,
    resume_data,
    job_description,
    analysis_data,
    similarity_score,
    ats_result
):
    """
    Save complete resume analysis into SQLite database.
    Parameters
    ----------
    user_id : int
        Logged in user ID.

    resume_filename : str
        Uploaded PDF filename.

    resume_filepath : str
        Location where PDF is stored.

    resume_text : str
        Extracted resume text.

    resume_data : dict
        Structured resume information from Gemini.

    job_description : str
        User entered job description.

    analysis_data : dict
        Gemini analysis result.

    similarity_score : float
        TF-IDF similarity score.

    ats_result : dict
        ATS score and breakdown.
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 1. Save Resume
        cursor.execute(
            """
            INSERT INTO resumes
            (
                user_id,
                file_name,
                file_path,
                resume_text,
                candidate_name,
                email,
                phone
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                resume_filename,
                resume_filepath,
                resume_text,
                resume_data.get("name", ""),
                resume_data.get("email", ""),
                resume_data.get("phone", "")
            )
        )

        resume_id = cursor.lastrowid
        # 2. Save Job Description
        cursor.execute(
            """
            INSERT INTO job_descriptions
            (
                user_id,
                company_name,
                job_role,
                description
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                analysis_data.get("company_name", ""),
                analysis_data.get("job_title", "Unknown"),
                job_description
            )
        )

        job_description_id = cursor.lastrowid
        # 3. Save Resume Skills
        for skill in resume_data.get("skills", []):
            cursor.execute(
                """
                INSERT INTO extracted_skills
                (
                    resume_id,
                    skill_name,
                    skill_type
                )
                VALUES (?, ?, ?)
                """,
                (
                    resume_id,
                    skill,
                    "Resume"
                )
            )

        # 4. Save Analysis Result
        cursor.execute(
            """
            INSERT INTO analysis_results
            (
                user_id,
                resume_id,
                job_description_id,
                ats_score,
                similarity_score,
                overall_score,
                matched_skills,
                missing_skills,
                strengths,
                weaknesses,
                recommendations,
                overall_summary,
                score_breakdown
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                resume_id,
                job_description_id,
                ats_result["ats_score"],
                similarity_score,
                ats_result["ats_score"],
                json.dumps(analysis_data.get("matched_skills",[])),

                json.dumps(analysis_data.get("missing_required_skills",analysis_data.get("missing_skills",[]))),

                json.dumps(analysis_data.get("strengths",[])),

                json.dumps(analysis_data.get("weaknesses",[])),

                json.dumps(analysis_data.get("recommendations",[])),

                analysis_data.get("overall_summary",""),

                json.dumps(ats_result.get("breakdown",{}))
            )
        )

        analysis_result_id = cursor.lastrowid

        # 5. Save History
        cursor.execute(
            """
            INSERT INTO analysis_history
            (
                user_id,
                analysis_result_id
            )
            VALUES (?, ?)
            """,
            (
                user_id,
                analysis_result_id
            )
        )

        conn.commit()
        return analysis_result_id

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()