import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "meta-llama/llama-4-maverick-17b-128e-instruct"


def extract_structured_data(text: str):

    system_prompt = """
You are a strict JSON extraction engine.
You must ALWAYS return valid JSON.
Do not return explanations.
Do not return markdown.
Do not return extra text.
Only return valid parsable JSON.
All values must be strings.
"""

    user_prompt = f"""
Extract the following from the resume text:

1. Skills (comma-separated string)
2. YearsOfExperience (total years as string)
3. DegreeDetails (format: Degree - Specialization - University - Year)

If Skills or DegreeDetails are missing return "Not Found".
If YearsOfExperience is missing return -1.

Return EXACTLY in this format:

{{
  "Skills": "string",
  "YearsOfExperience": number,
  "DegreeDetails": "string"
}}

Resume Text:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        top_p=1,
        max_tokens=500
    )

    output_text = response.choices[0].message.content.strip()

    try:
        return json.loads(output_text)
    except json.JSONDecodeError:
        print("Raw model output:", output_text)
        return {
            "Skills": "Not Found",
            "YearsOfExperience": 0,
            "DegreeDetails": "Not Found"
        }