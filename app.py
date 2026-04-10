from flask import Flask, request, jsonify
from utils.pdf_reader import read_pdf
from parser.resume_parser import parse_resume
from parser.jd_parser import parse_jd
from matcher.skill_matcher import match_skills

app = Flask(__name__)

@app.route("/match", methods=["POST"])
def match():
    resume_file = request.files["resume"]
    jd_file = request.files["jd"]

    resume_path = "temp_resume.pdf"
    jd_path = "temp_jd.pdf"

    resume_file.save(resume_path)
    jd_file.save(jd_path)

    resume_text = read_pdf(resume_path)
    jd_text = read_pdf(jd_path)

    resume_data = parse_resume(resume_text)
    jd_data = parse_jd(jd_text)

    skills_analysis, score = match_skills(
        jd_data["skills"],
        resume_data["resumeSkills"]
    )

    response = {
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

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)