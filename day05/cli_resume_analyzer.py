"""
Day 5 Project: CLI Resume Skill Gap Analyzer v0.5

Goal:
Accept resume file, required skills file, and output JSON file path
from command-line arguments.

Role Target:
LLM Application Developer / GenAI Application Developer
"""

import argparse
import json
from pathlib import Path


def read_text_file(file_path):
    """
    Read and return text from a file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, but got a folder: {path}")

    return path.read_text(encoding="utf-8")


def read_required_skills(file_path):
    """
    Read required skills from a text file.

    Each skill must be written on a separate line.
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

    print("===== CLI Resume Skill Gap Analyzer v0.5 =====")
    print()
    print("Target Role:", analysis_result["target_role"])
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

    output_path = Path(output_file)

    if output_path.parent:
        output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(analysis_result, file, indent=4)

    print()
    print("JSON report saved successfully:", output_path)


def parse_arguments():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Analyze resume skill gaps for an LLM/GenAI Application Developer role."
    )

    parser.add_argument(
        "--resume",
        required=True,
        help="Path to the resume text file.",
    )

    parser.add_argument(
        "--skills",
        required=True,
        help="Path to the required skills text file.",
    )

    parser.add_argument(
        "--output",
        default="day05/cli_resume_report.json",
        help="Path where the JSON report should be saved.",
    )

    return parser.parse_args()


def main():
    """
    Main function that controls the CLI program flow.
    """

    args = parse_arguments()

    resume_text = read_text_file(args.resume)
    required_skills = read_required_skills(args.skills)

    analysis_result = analyze_resume(resume_text, required_skills)

    analysis_result["resume_source"] = args.resume
    analysis_result["skills_source"] = args.skills
    analysis_result["output_file"] = args.output

    display_report(analysis_result)
    save_report_to_json(analysis_result, args.output)


if __name__ == "__main__":
    main()