"""
Day 3 Project: Structured Resume Skill Gap Report v0.3

Goal:
Analyze multiple resume profiles and save the result as structured JSON.

Role Target:
LLM Application Developer / GenAI Application Developer
"""

import json


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


def analyze_resume(candidate_name, resume_text, required_skills):
    """
    Analyze one candidate resume against required skills.

    Parameters:
    candidate_name: Name of the candidate/profile.
    resume_text: Resume or profile summary text.
    required_skills: List of required skills.

    Returns:
    A dictionary containing structured analysis result.
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
        "candidate_name": candidate_name,
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


def display_report(analysis_results):
    """
    Display multiple candidate reports in the terminal.
    """

    print("===== Structured Resume Skill Gap Report v0.3 =====")
    print()

    for result in analysis_results:
        print("Candidate:", result["candidate_name"])
        print("Target Role:", result["target_role"])
        print("Match Score:", result["match_score"], "%")
        print("Recommendation:", result["recommendation"])

        print("Matched Skills:")
        for skill in result["matched_skills"]:
            print("-", skill)

        print("Missing Skills:")
        for skill in result["missing_skills"]:
            print("-", skill)

        print("-" * 50)


def save_report_to_json(analysis_results, file_name):
    """
    Save analysis results into a JSON file.
    """

    with open(file_name, "w") as file:
        json.dump(analysis_results, file, indent=4)

    print()
    print("JSON report saved successfully:", file_name)


def main():
    """
    Main function that controls the program flow.
    """

    required_skills = [
        "Python",
        "FastAPI",
        "REST API",
        "Prompt Engineering",
        "LLM",
        "Embeddings",
        "Vector Database",
        "RAG",
        "Git",
        "Docker",
        "LangChain",
        "LlamaIndex",
        "PostgreSQL",
        "Cloud Deployment",
        "AI Agents",
        "Streamlit",
    ]

    candidate_profiles = [
        {
            "candidate_name": "Main Learning Profile",
            "resume_text": """
            I am learning Python, FastAPI, REST API development, LLM applications,
            prompt engineering, RAG, embeddings, vector databases, Git, Docker,
            LangChain, PostgreSQL, AI Agents, Cloud Deployment, LlamaIndex, and Streamlit.
            I want to build AI applications using APIs and real-world documents.
            """,
        },
        {
            "candidate_name": "Beginner Profile",
            "resume_text": """
            I am learning Python and Git.
            I am new to AI applications.
            """,
        },
        {
            "candidate_name": "Backend-Oriented AI Profile",
            "resume_text": """
            I have experience with Python, REST API development, PostgreSQL,
            Docker, Cloud Deployment, FastAPI, and Git.
            I am starting to learn LLM applications and prompt engineering.
            """,
        },
        {
            "candidate_name": "RAG Focused Profile",
            "resume_text": """
            I am learning Python, FastAPI, LLM applications, prompt engineering,
            embeddings, vector databases, RAG, LangChain, LlamaIndex, Git, and Docker.
            """,

        },
    ]

    analysis_results = []

    for profile in candidate_profiles:
        result = analyze_resume(
            profile["candidate_name"],
            profile["resume_text"],
            required_skills,
        )

        analysis_results.append(result)

    display_report(analysis_results)
    save_report_to_json(analysis_results, "day03/resume_analysis_report.json")


if __name__ == "__main__":
    main()