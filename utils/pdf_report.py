from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(ats, llm):

    path = "reports/resume_report.pdf"

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>AI Resume Analysis Report</b>",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"ATS Score: {ats['ats_score']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Semantic Match: {ats['semantic_score']}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Summary</b><br/>{llm['summary']}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Suggestions</b><br/>"
            + "<br/>".join(llm["suggestions"]),
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return path