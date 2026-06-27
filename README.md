# 🚀 ResumeIQ – AI-Powered Resume Analyzer

ResumeIQ is an intelligent web application that analyzes resumes against job descriptions using **AI + NLP**, evaluates **ATS (Applicant Tracking System) compatibility**, and provides actionable improvement suggestions powered by **Google Gemini AI**.

It helps job seekers optimize resumes to increase interview selection chances.

---

## ✨ Features

- 📄 Upload resume (PDF only)
- 🧠 Extract structured text using PyMuPDF
- 💬 AI-powered analysis using Google Gemini API
- 📊 ATS score generation with weighted scoring system
- 🧩 Skill extraction (technical + soft skills)
- 🔍 Job Description vs Resume matching
- 📈 Personalized improvement suggestions
- 📋 Interactive dashboard with visual insights

---

## 🏗️ Tech Stack

### 🔹 Frontend
| Technology | Purpose |
|------------|--------|
| HTML       | Structure of UI |
| CSS        | Styling and layout |
| JavaScript | Dynamic dashboard & interactions |

### 🔹 Backend
| Technology | Purpose |
|------------|--------|
| Python     | Core backend logic |
| Flask      | Web framework & routing |

### 🔹 AI / Machine Learning
| Technology | Purpose |
|------------|--------|
| Google Gemini API | Resume analysis, skill extraction, JD matching |
| NLP Techniques | Text similarity & keyword extraction |
| TF-IDF | Resume–JD similarity scoring |

### 🔹 PDF Processing
| Technology | Purpose |
|------------|--------|
| PyMuPDF (fitz) | Extract text from uploaded PDF resumes |

---

## 🧠 How It Works

1. User uploads a **PDF resume**
2. Job Description is entered in a text box
3. Resume text is extracted using **PyMuPDF**
4. Backend processes data and sends it to **Gemini AI**
5. AI extracts:
   - Skills
   - Experience level
   - Education
   - Projects
   - Strengths & weaknesses
6. ATS score is computed using weighted algorithm
7. Results are displayed in a dashboard with visual insights

---

## 📊 ATS Scoring System

| Component         | Weight (%) |
|------------------|------------|
| TF-IDF Similarity| 40%        |
| Skill Match      | 30%        |
| Projects         | 10%        |
| Experience       | 10%        |
| Education        | 5%         |
| Certifications   | 5%         |
| **Total**        | **100%**   |

---

## 📁 Project Structure
RESUMEIQ/
│
├── database/
│   ├── database.db
│   ├── database.py
│   ├── save_analysis.py
│   └── schema.sql
│
├── routes/
│   ├── analysis.py
│   ├── auth.py
│   └── dashboard.py
│
├── services/
│   ├── ats_service.py
│   ├── gemini_service.py
│   ├── pdf_parser.py
│   └── similarity.py
│
├── static/
│   ├── css/
│   │   ├── auth.css
│   │   └── dashboard.css
│   └── js/
│       └── dashboard.js
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── uploads/
├── app.py
├── requirements.txt
├── .env
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/your-username/resumeiq.git
cd resumeiq

---

### 2️⃣ Create Virtual Environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here

---

### 5️⃣ Run Application
python app.py

---

## 🌐 Open in Browser
http://127.0.0.1:5000

---

## 📌 Future Improvements

- JWT-based authentication system  
- Advanced analytics dashboard  
- Multi-language resume support  
- Multi-model AI comparison (Gemini + OpenAI)  
- Cloud deployment (AWS / Render)

---

## 👨‍💻 Developed by
Devansh Mankad 
---

## 📜 License
This project is licensed under the MIT License.
