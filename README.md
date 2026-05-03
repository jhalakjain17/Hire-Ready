HireReady is an intelligent resume analysis tool powered by Large Language Models (LLMs). It helps job seekers improve their resumes by providing ATS scores, skill extraction, and personalized suggestions.

🚀 Features:-

📊 ATS Score Calculation
Evaluate how well your resume performs with Applicant Tracking Systems.
🧠 LLM-Based Analysis
Uses AI to deeply analyze resume content and structure.
🛠 Skill Extraction
Automatically detects technical and soft skills from your resume.
💡 Smart Suggestions
Get personalized recommendations to improve your resume.
📄 PDF Resume Upload
Upload and analyze resumes easily.
⚡ Fast & User-Friendly UI
Built with Streamlit for a smooth experience.

🛠 Tech Stack:-

Frontend: Streamlit
Backend: Python
Libraries:
PyMuPDF (PDF processing)
AI Model: LLM (via Ollama / OpenAI API)


Run the code:-

Use : streamlit run app.py

Production  Folder Structure:-

resume-analyzer/
│
├── app.py
├── requirements.txt
├── utils/
|   |---_.init_.py
│   ├---parser.py
│   |--ats.py
│   |-- llm.py
│   ├-- prompts.py
│   └-- pdf_report.py
│
├── assets/
│   └── style.css
│
└── reports/ 

#Create a folder which contain your API key 
.streamlit/secrets.toml
OPENROUTER_API_KEY = "your_api_key_here"