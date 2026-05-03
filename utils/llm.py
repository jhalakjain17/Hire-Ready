from openai import OpenAI
import streamlit as st
import json

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]  # FIXED
)

MODEL_NAME = "openai/gpt-3.5-turbo"  # safer model

SYSTEM_PROMPT = """
You are an expert ATS resume analyzer.

Return ONLY valid JSON.

Schema:
{
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "suggestions": [],
    "ats_improvements": []
}
"""

def analyze_resume_llm(resume, jd):

    prompt = f"""
Resume:
{resume}

Job Description:
{jd}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "summary": content,
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "ats_improvements": []
        }