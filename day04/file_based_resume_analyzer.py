"""
Day 4 Project: File-Based Resume Skill Gap Analyzer v0.4

Goal:
Read resume text and required skills from external text files,
analyze the resume, and save the result as JSON.

Role Target:
LLM Application Developer / GenAI Application Developer
"""

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"

RESUME_FILE = INPUT_DIR / "resume.txt"
REQUIRED_SKILLS_FILE = INPUT_DIR / "required_skills.txt"
OUTPUT_FILE = BASE_DIR / "resume_file_report.json"


def read_text_file(file_path):
    """
    Read and return text from a file.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def read_required_skills(file_path):
    """
    Read required skills from a text file.

    Each skill should be written on a separate line.
    Empty lines are ignored.
    """

    file_content = read_text_file(file_path)

    skills = []

    for line in file_content.splitlines():
        cleaned_skill = line.strip()

        if cleaned_skill:
            skills.append(cleaned_skill)

    return skills


def get_recommendation(match_score):
    """
    Return a recommendation based on the match score.
    """

    if match_score >= 80:
        return "Strong match. Continue building portfolio projects."
    elif match_score >= 50:
        return "Moderate match. Improve missing technical skills."
    else:
        return "Beginner level. Focus on foundation skills first."


def analyze_resume(resume_text, required_skills):
    """
    Analyze resume text against required skills.
    """

    matched_skills = []
    missing_skills = []

    normalized_resume_text = resume_text.lower()

    for skill in required_skills:
        if skill.lower() in normalized_resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) == 0:
        match_score = 0
    else:
        match_score = (len(matched_skills) / len(required_skills)) * 100

    rounded_score = round(match_score, 2)

    result = {
        "target_role": "LLM Application Developer / GenAI Application Developer",
        "resume_source": str(RESUME_FILE),
        "skills_source": str(REQUIRED_SKILLS_FILE),
        "total_required_skills": len(required_skills),
        "matched_count": len(matched_skills),
        "missing_count": len(missing_skills),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": rounded_score,
        "recommendation": get_recommendation(rounded_score),
    }

    return result


def display_report(analysis_result):
    """
    Display analysis result in the terminal.
    """

    print("===== File-Based Resume Skill Gap Analyzer v0.4 =====")
    print()
    print("Target Role:", analysis_result["target_role"])
    print("Resume Source:", analysis_result["resume_source"])
    print("Skills Source:", analysis_result["skills_source"])
    print()

    print("Matched Skills:")
    for skill in analysis_result["matched_skills"]:
        print("-", skill)

    print()

    print("Missing Skills:")
    for skill in analysis_result["missing_skills"]:
        print("-", skill)

    print()
    print("Matched Count:", analysis_result["matched_count"])
    print("Missing Count:", analysis_result["missing_count"])
    print("Match Score:", analysis_result["match_score"], "%")
    print("Recommendation:", analysis_result["recommendation"])


def save_report_to_json(analysis_result, output_file):
    """
    Save analysis result into a JSON file.
    """

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(analysis_result, file, indent=4)

    print()
    print("JSON report saved successfully:", output_file)


def main():
    """
    Main function that controls the program flow.
    """

    resume_text = read_text_file(RESUME_FILE)
    required_skills = read_required_skills(REQUIRED_SKILLS_FILE)

    analysis_result = analyze_resume(resume_text, required_skills)

    display_report(analysis_result)
    save_report_to_json(analysis_result, OUTPUT_FILE)


if __name__ == "__main__":
    main()