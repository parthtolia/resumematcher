from app.database import SessionLocal
from app.models.resume import Resume

def save_resume(data: dict, file_name: str, file_path: str, full_text: str, embedding: list):
    db = SessionLocal()

    resume = Resume(
        file_name=file_name,
        file_path=file_path,
        full_text=full_text,
        skills=data.get("Skills", "Not Found"),        #", ".join(data.get("skills", [])),
        total_experience=data.get("YearsOfExperience", 0),
        education_level=data.get("DegreeDetails", "Not Found"),
        embedding=embedding
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    db.close()

    return resume