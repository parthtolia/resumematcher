
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import json

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    device_map="auto"
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)


def extract_resume_data(resume_text: str):

    prompt = f"""
You are an intelligent HR system.

Extract the following fields from the resume:

1. skills (technical skills only, list format)
2. total_experience_years (number only)
3. education_level (High School, Diploma, Bachelors, Masters, PhD)

Return STRICT JSON only.

Resume:
\"\"\"{resume_text}\"\"\"
"""

    response = generator(
        prompt,
        max_new_tokens=300,
        temperature=0.1
    )

    output_text = response[0]["generated_text"]

    # Extract JSON safely
    try:
        json_start = output_text.find("{")
        json_end = output_text.rfind("}") + 1
        structured_data = json.loads(output_text[json_start:json_end])
    except:
        structured_data = {
            "skills": [],
            "total_experience_years": 0,
            "education_level": "Unknown"
        }

    return structured_data