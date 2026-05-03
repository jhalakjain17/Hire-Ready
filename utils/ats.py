from sentence_transformers import SentenceTransformer, util

SKILLS_DB = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "react",
    "html",
    "css",
    "streamlit",
    "flask",
    "django",
    "aws",
    "docker",
    "git"
]

class ATSAnalyzer:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def analyze(self, resume, jd):

        resume_lower = resume.lower()
        jd_lower = jd.lower()

        matched = [
            skill for skill in SKILLS_DB
            if skill in resume_lower
        ]

        jd_skills = [
            skill for skill in SKILLS_DB
            if skill in jd_lower
        ]

        missing = list(
            set(jd_skills) - set(matched)
        )

        # Semantic similarity
        emb1 = self.model.encode(
            resume,
            convert_to_tensor=True
        )

        emb2 = self.model.encode(
            jd,
            convert_to_tensor=True
        )

        similarity = int(
            util.cos_sim(emb1, emb2).item() * 100
        )

        ats_score = min(
            int(
                (len(matched) / len(SKILLS_DB)) * 100
            ),
            100
        )

        return {
            "ats_score": ats_score,
            "semantic_score": similarity,
            "matched_skills": matched,
            "missing_skills": missing
        }