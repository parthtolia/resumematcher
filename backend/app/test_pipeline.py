from pdf_parser import extract_text_from_pdf
from groq_service import extract_structured_data
from embeddings import generate_embedding
from services.resume_service import save_resume

pdf_path = "resumes/Pritha Datta - AI & Data Science.pdf"

# Step 1: Extract text
text = extract_text_from_pdf(pdf_path)

# Step 2: Extract structured data using Groq
structured_data = extract_structured_data(text)

# Step 3: Generate embedding
embedding = generate_embedding(text)

# Step 4: Save into database
save_resume(
    data=structured_data,
    file_name="Pritha Datta - AI & Data Science.pdf",
    file_path=pdf_path,
    full_text=text,
    embedding=embedding
)

print("Resume processed and stored successfully!")