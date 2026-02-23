from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.pdf_parser import extract_text_from_pdf
from app.groq_service import extract_structured_data
from app.embeddings import generate_embedding
from app.services.resume_service import save_resume
from app.services.match_service import match_resumes
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app = FastAPI()

UPLOAD_FOLDER = "uploaded_resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# 1️⃣ Upload Resume Endpoint
# ----------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    print("Received file:", file.filename, file.content_type)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Groq structured extraction
    structured_data = extract_structured_data(text)

    # Generate embedding
    embedding = generate_embedding(text)

    # Save to DB
    resume = save_resume(
        data=structured_data,
        file_name=file.filename,
        file_path=file_path,
        full_text=text,
        embedding=embedding
    )

    return {
        "message": "Resume uploaded successfully",
        "resume_id": str(resume.id)
    }


# ----------------------------
# 2️⃣ Match Endpoint
# ----------------------------
class JDRequest(BaseModel):
    jd_text: str

@app.post("/match")
async def match(request: JDRequest):
    results = match_resumes(request.jd_text)

    return {
        "total_matches": len(results),
        "results": results
    }