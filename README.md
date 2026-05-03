HireReady is an intelligent resume analysis tool powered by Large Language Models (LLMs). It helps job seekers improve their resumes by providing ATS scores, skill extraction, and personalized suggestions.

🚀 Features:-

📊 ATS Score Calculation <br>
Evaluate how well your resume performs with Applicant Tracking Systems.<br>
🧠 LLM-Based Analysis <br>
Uses AI to deeply analyze resume content and structure.<br>
🛠 Skill Extraction<br>
Automatically detects technical and soft skills from your resume.<br>
💡 Smart Suggestions<br>
Get personalized recommendations to improve your resume.<br>
📄 PDF Resume Upload<br>
Upload and analyze resumes easily.<br>
⚡ Fast & User-Friendly UI<br>
Built with Streamlit for a smooth experience.<br>

🛠 Tech Stack:-

Frontend: Streamlit <br>
Backend: Python <br>
Libraries: <br>
PyMuPDF (PDF processing)<br>
AI Model: LLM (via Ollama / OpenAI API)<br>


Run the code:-

Use : streamlit run app.py

Production  Folder Structure:-

resume-analyzer/
│
├── app.py <br>
├── requirements.txt <br>
├── utils/ <br>
|   |---_.init_.py <br>
│   ├---parser.py <br>
│   |--ats.py <br>
│   |-- llm.py <br>
│   ├-- prompts.py <br>
│   └-- pdf_report.py <br>
│
├── assets/ <br>
│   └── style.css <br>
│
└── reports/   <br>

#Create a folder which contain your API key  <br>
.streamlit/secrets.toml <br>
OPENROUTER_API_KEY = "your_api_key_here" <br>