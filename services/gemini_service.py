def calculate_ats_score(similarity_score,resume_data,analysis_data):
    """
    Calculate ATS Score.
    Parameters
    ----------
    similarity_score : float
        TF-IDF similarity percentage.

    resume_data : dict
        Resume information extracted by Gemini.

    analysis_data : dict
        Resume analysis returned by Gemini.
    Returns
    -------
    dict
        ATS score with detailed breakdown.
    """

    # Similarity (40 Marks)
    similarity_marks = (similarity_score / 100) * 40

    # Skill Match (30 Marks)
    required_skills = analysis_data.get("required_skills",[])
    matched_skills = analysis_data.get("matched_skills",[])
    if required_skills:
        skill_ratio = len(matched_skills) / len(required_skills)
        skill_marks = skill_ratio * 30
    else:
        skill_marks = 30

    # Projects (10 Marks)
    projects = resume_data.get("projects",[])

    if len(projects) >= 3:
        project_marks = 10
    elif len(projects) == 2:
        project_marks = 8
    elif len(projects) == 1:
        project_marks = 5
    else:
        project_marks = 0

    # Experience (10 Marks)
    experience = resume_data.get("experience",[])
    if len(experience) >= 2:
        experience_marks = 10
    elif len(experience) == 1:
        experience_marks = 6
    else:
        experience_marks = 3

    # Education (5 Marks)
    education = resume_data.get("education",[])
    education_marks = 5 if education else 0

    # Certifications (5 Marks)
    certifications = resume_data.get("certifications",[])
    certification_marks = min(len(certifications),5)

    # Missing Required Skill Penalty
    missing_required = analysis_data.get(
        "missing_skills",
        []
    )

    penalty = len(missing_required) * 5
    penalty = min(penalty,20)

    # Final Score
    total_score = round(

        similarity_marks
        + skill_marks
        + project_marks
        + experience_marks
        + education_marks
        + certification_marks
        - penalty,
        2
    )

    total_score = max(0,min(total_score,100))

    return {
        "ats_score": total_score,
        "breakdown": {
            "similarity": round(
                similarity_marks,
                2
            ),
            "skills": round(
                skill_marks,
                2
            ),
            "projects": project_marks,
            "experience": experience_marks,
            "education": education_marks,
            "certifications": certification_marks,
            "penalty": penalty
        },
        "missing_required_skills": missing_required
    }