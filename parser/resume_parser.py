import re
from utils.text_cleaner import clean_text
from data.skills import SKILLS

def extract_name(text):
    lines = text.split("\n")
    return lines[0].strip() if lines else "Unknown"

def extract_skills(text):
    text = clean_text(text)
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))

def extract_experience(text):
    pattern = r'(\d+)\+?\s?(years|year)'
    matches = re.findall(pattern, text)

    if matches:
        return max([int(x[0]) for x in matches])
    return 0

def parse_resume(text):
    return {
        "name": extract_name(text),
        "resumeSkills": extract_skills(text),
        "yearOfExperience": extract_experience(text)
    }