import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def extract_resume_information(resume_text):
    """
    Extract structured information from resume using Gemini.
    """
    prompt = f"""
You are an expert Resume Parser.
Extract the resume information and return ONLY valid JSON.
Required JSON format:
{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Resume:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()
        return json.loads(text)

    except Exception as e:
        print("Gemini Resume Extraction Error:", e)
        return {
            "name": "",
            "email": "",
            "phone": "",
            "skills": [],
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": []
        }

def analyze_resume(resume_data, job_description):
    """
    Compare resume against job description.
    """
    prompt = f"""
You are an ATS Resume Expert.
Compare the following resume with the job description.
Return ONLY valid JSON.
JSON Format:
{{
    "company_name": "",
    "job_title": "",
    "required_skills": [],
    "preferred_skills": [],
    "matched_skills": [],
    "missing_required_skills": [],
    "strengths": [],
    "weaknesses": [],
    "recommendations": [],
    "overall_summary": ""
}}

Resume:
{json.dumps(resume_data, indent=2)}
Job Description:
{job_description}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()
        return json.loads(text)

    except Exception as e:
        print("Gemini Analysis Error:", e)
        return {
            "company_name": "",
            "job_title": "Unknown",
            "required_skills": [],
            "preferred_skills": [],
            "matched_skills": [],
            "missing_required_skills": [],
            "strengths": [],
            "weaknesses": [],
            "recommendations": [],
            "overall_summary": "Unable to analyze resume."
        }