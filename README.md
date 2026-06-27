# 🚀 ResumeIQ - AI-Powered Resume Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge\&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge\&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered Resume Analysis Platform that evaluates resumes using ATS scoring, semantic similarity, skill-gap detection, and Google Gemini AI.**

</div>

---

# 📖 Overview

ResumeIQ is an intelligent resume analysis platform built using **Flask**, **SQLite**, and **Google Gemini AI**. It helps job seekers evaluate how well their resumes match a given job description by combining traditional ATS techniques with AI-powered analysis.

Instead of relying only on keyword matching, ResumeIQ performs:

* AI Resume Parsing
* Semantic Resume Matching
* ATS Score Calculation
* Skill Gap Detection
* AI-Based Resume Feedback
* Resume Analysis History

---

# ✨ Features

### 👤 Authentication

* User Registration
* Secure Login
* Password Hashing
* Session Management

---

### 📄 Resume Processing

* Upload PDF Resume
* Extract Resume Text
* Resume Information Parsing
* Candidate Information Extraction

---

### 🤖 AI Analysis

Powered by **Google Gemini AI**

ResumeIQ extracts:

* Skills
* Projects
* Experience
* Education
* Certifications

It also generates:

* Resume Strengths
* Resume Weaknesses
* Missing Skills
* Personalized Recommendations
* Overall Resume Summary

---

### 📊 ATS Score

ResumeIQ calculates an ATS score using multiple factors:

| Factor                 | Weight    |
| ---------------------- | --------- |
| Resume Similarity      | 40%       |
| Skill Match            | 30%       |
| Projects               | 10%       |
| Experience             | 10%       |
| Education              | 5%        |
| Certifications         | 5%        |
| Missing Skills Penalty | Up to -20 |

---

### 📈 Dashboard

Interactive dashboard showing:

* ATS Score
* Resume Match Score
* Skill Match Analysis
* ATS Breakdown
* Resume Recommendations
* Analysis Charts

---

### 📚 Analysis History

Each resume analysis is stored for future reference.

Users can view:

* Job Role
* ATS Score
* Similarity Score
* Analysis Date
* Previous Results

---

# 🏗️ Project Structure

```text
ResumeIQ/
│
├── app.py
│
├── database/
│   ├── database.py
│   ├── save_analysis.py
│   ├── schema.sql
│   └── database.db (generated locally)
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── analysis.py
│   └── history.py
│
├── services/
│   ├── pdf_parser.py
│   ├── gemini_service.py
│   ├── similarity.py
│   └── ats_service.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── uploads/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Tech Stack

### Backend

* Python
* Flask

### Database

* SQLite

### AI

* Google Gemini API

### Machine Learning

* TF-IDF Vectorizer
* Cosine Similarity

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap Icons
* Plotly.js

### Libraries

* PyMuPDF
* Scikit-learn
* Werkzeug

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ResumeIQ.git

cd ResumeIQ
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Initialize Database

```bash
python app.py
```

---

## Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 📊 Workflow

```text
User Uploads Resume
        │
        ▼
Extract PDF Text
        │
        ▼
Gemini Resume Parsing
        │
        ▼
Semantic Similarity
        │
        ▼
ATS Score Calculation
        │
        ▼
AI Recommendation
        │
        ▼
Save Analysis
        │
        ▼
Dashboard + Charts
```

---

# 📸 Screenshots

Add screenshots here:

* Login Page
<img width="1903" height="918" alt="image" src="https://github.com/user-attachments/assets/ba69d8be-cd3a-44e1-bc2d-76a1e34cf212" />
 
* Registration Page
<img width="1900" height="922" alt="image" src="https://github.com/user-attachments/assets/d1a30b84-ddba-4945-9b54-73692e0a7f61" />

* Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fb10a6a4-15c1-4ab4-9243-f4a7f82f6a4a" />


* ATS Result
* Charts
* History Page
<img width="1530" height="638" alt="image" src="https://github.com/user-attachments/assets/c55723d3-8b6b-4a9f-9c96-d169fbf27556" />


---

# 🎯 Future Enhancements

* Resume PDF Report Export
* Resume Optimization Suggestions
* Multiple Resume Comparison
* Recruiter Dashboard
* AI Resume Builder
* Cover Letter Generator
* Interview Question Generator
* Email Resume Sharing
* Cloud Database Support

---

# 👨‍💻 Author

**Devansh Mankad**

Computer Engineering Student

* GitHub: https://github.com/Devansh-Mankad
---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
