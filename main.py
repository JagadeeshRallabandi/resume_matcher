from utils.pdf_reader import read_pdf
from parser.resume_parser import parse_resume
from parser.jd_parser import parse_jd
from matcher.skill_matcher import match_skills

def run(resume_path, jd_path):
    resume_text = read_pdf(resume_path)
    jd_text = read_pdf(jd_path)

    resume_data = parse_resume(resume_text)
    jd_data = parse_jd(jd_text)

    skills_analysis, score = match_skills(
        jd_data["skills"],
        resume_data["resumeSkills"]
    )

    output = {
        "name": resume_data["name"],
        "salary": jd_data["salary"],
        "yearOfExperience": resume_data["yearOfExperience"],
        "resumeSkills": resume_data["resumeSkills"],
        "matchingJobs": [
            {
                "jobId": jd_data["jobId"],
                "role": "Software Developer",
                "aboutRole": jd_data["aboutRole"],
                "skillsAnalysis": skills_analysis,
                "matchingScore": score
            }
        ]
    }

    return output


if __name__ == "__main__":
    result = run("resume.pdf", "jd.pdf")
    print(result)