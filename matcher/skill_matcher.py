def match_skills(jd_skills, resume_skills):
    result = []
    matched = 0

    for skill in jd_skills:
        present = skill in resume_skills
        if present:
            matched += 1

        result.append({
            "skill": skill,
            "presentInResume": present
        })

    score = (matched / len(jd_skills)) * 100 if jd_skills else 0

    return result, round(score, 2)