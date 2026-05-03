
import streamlit as st
from utils.parser import extract_resume_text
from utils.ats import ATSAnalyzer
from utils.llm import analyze_resume_llm
from utils.pdf_report import generate_pdf

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file and job_description:

    with st.spinner("Analyzing Resume..."):

        # Extract text
        resume_text = extract_resume_text(uploaded_file)

        # ATS Engine
        ats = ATSAnalyzer()

        ats_result = ats.analyze(
            resume_text,
            job_description
        )

        # LLM Analysis
        llm_result = analyze_resume_llm(
            resume_text,
            job_description
        )

        # UI
        col1, col2 = st.columns(2)

        col1.metric(
            "ATS Score",
            ats_result["ats_score"]
        )

        col2.metric(
            "Semantic Match",
            ats_result["semantic_score"]
        )

        st.progress(ats_result["ats_score"] / 100)

        st.subheader("Matched Skills")
        st.write(ats_result["matched_skills"])

        st.subheader("Missing Skills")
        st.write(ats_result["missing_skills"])

        st.subheader("Professional Summary")
        st.write(llm_result["summary"])

        st.subheader("Strengths")
        st.write(llm_result["strengths"])

        st.subheader("Weaknesses")
        st.write(llm_result["weaknesses"])

        st.subheader("Suggestions")
        st.write(llm_result["suggestions"])

        pdf_path = generate_pdf(
            ats_result,
            llm_result
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                "Download Report",
                f,
                file_name="resume_report.pdf"
            )