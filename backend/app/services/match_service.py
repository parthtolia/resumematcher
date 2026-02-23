from sqlalchemy import text
from app.database import SessionLocal
from app.embeddings import generate_embedding

def match_resumes(jd_text: str):

    jd_embedding = generate_embedding(jd_text)
    jd_vector_str = "[" + ",".join(map(str, jd_embedding)) + "]"

    db = SessionLocal()

    query = text("""
        SELECT id,
               file_name,
               skills,
               total_experience,
               education_level,
               1 - (embedding <=> CAST(:jd_vector AS vector)) AS semantic_score
        FROM resumes
        LIMIT 10;
    """)

    results = db.execute(query, {
        "jd_vector": jd_vector_str
    }).fetchall()

    db.close()

    final_results = []

    for row in results:

        skill_score = calculate_skill_match(row.skills, jd_text)

        # Weighted scoring
        final_score = (
            0.6 * row.semantic_score +
            0.4 * skill_score
        )

        final_results.append({
            "file_name": row.file_name,
            "semantic_score": round(row.semantic_score, 3),
            "skill_score": round(skill_score, 3),
            "final_score": round(final_score, 3)
        })

    # Sort by final score
    final_results.sort(key=lambda x: x["final_score"], reverse=True)

    return final_results



def calculate_skill_match(resume_skills: str, jd_text: str):

    if not resume_skills:
        return 0

    resume_skill_list = [s.strip().lower() for s in resume_skills.split(",")]
    jd_lower = jd_text.lower()

    matched = [skill for skill in resume_skill_list if skill in jd_lower]

    if len(resume_skill_list) == 0:
        return 0

    return len(matched) / len(resume_skill_list)


