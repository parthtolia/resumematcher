from sqlalchemy import text
from embeddings import generate_embedding
from database import SessionLocal

jd_text = "Generative AI, LLMs, RAG, Semantic Search, Prompt Engineering, LangChain, Embedding Models, Time Series Forecasting, Regression, Classification"
jd_embedding = generate_embedding(jd_text)

db = SessionLocal()

query = text("""
SELECT file_name,
       1 - (embedding <=> CAST(:jd_vector AS vector)) AS similarity
FROM resumes;
""")

result = db.execute(query, {
    "jd_vector": jd_embedding
}).fetchall()

print("Result = ",result)

for row in result:
    print(row)

db.close()