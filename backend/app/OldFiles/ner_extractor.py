
from transformers import pipeline
import re
from datetime import datetime

# Load once globally (important for performance)
ner_pipeline = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_resume_data(resume_text: str):

    entities = ner_pipeline(resume_text)

    skills = []
    organizations = []
    dates = []
    education_level = "Unknown"

    for entity in entities:
        label = entity["entity_group"]
        word = entity["word"]

        if label == "ORG":
            organizations.append(word)

        elif label == "DATE":
            dates.append(word)

        elif label == "MISC":
            skills.append(word)

    # ---- Simple education detection ----
    if re.search(r"\bPhD\b", resume_text, re.IGNORECASE):
        education_level = "PhD"
    elif re.search(r"\bMaster", resume_text, re.IGNORECASE):
        education_level = "Masters"
    elif re.search(r"\bBachelor", resume_text, re.IGNORECASE):
        education_level = "Bachelors"
    elif re.search(r"\bDiploma\b", resume_text, re.IGNORECASE):
        education_level = "Diploma"

    # ---- Simple experience estimation ----
    total_experience_years = estimate_experience_years(dates)

    return {
        "skills": list(set(skills)),
        "total_experience_years": total_experience_years,
        "education_level": education_level
    }


def estimate_experience_years(dates):
    years = []

    for date in dates:
        matches = re.findall(r"\b(19|20)\d{2}\b", date)
        years.extend(matches)

    if len(years) >= 2:
        years = sorted([int(y) for y in years])
        return max(years) - min(years)

    return 0