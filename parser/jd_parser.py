import re
from utils.text_cleaner import clean_text
from data.skills import SKILLS

def extract_salary(text):
    pattern = r'(\₹?\$?\d+[,\d]*\s?(lpa|per annum|year|usd)?)'
    match = re.search(pattern, text.lower())
    return match.group() if match else None

def extract_experience(text):
    pattern = r'(\d+)\+?\s?(years|year)'
    matches = re.findall(pattern, text.lower())

    if matches:
        return max([int(x[0]) for x in matches])
    return 0

def extract_skills(text):
    text = clean_text(text)
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))

def parse_jd(text, job_id="JD001"):
    return {
        "jobId": job_id,
        "salary": extract_salary(text),
        "yearOfExperience": extract_experience(text),
        "skills": extract_skills(text),
        "aboutRole": text[:300]
    }