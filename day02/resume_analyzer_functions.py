"""
Day 2 Project: Resume Skill Gap Analyzer v0.2

Goal:
Refactor the Day 1 script into reusable Python functions.

Role Target:
LLM Application Developer / GenAI Application Developer
"""


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
    Compare resume text with required skills.

    Parameters:
    resume_text: Text that represents the candidate's resume/profile.
    required_skills: List of skills needed for the target role.

    Returns:
    A dictionary containing matched skills, missing skills, match score,
    and recommendation.
    """

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_score = (len(matched_skills) / len(required_skills)) * 100
    recommendation = get_recommendation(match_score)

    result = {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": round(match_score, 2),
        "recommendation": recommendation,
    }

    return result


def display_report(analysis_result):
    """
    Display the resume analysis report in a readable format.
    """

    print("===== Resume Skill Gap Analyzer v0.2 =====")
    print()

    print("Matched Skills:")
    for skill in analysis_result["matched_skills"]:
        print("-", skill)

    print()

    print("Missing Skills:")
    for skill in analysis_result["missing_skills"]:
        print("-", skill)

    print()
    print("Match Score:", analysis_result["match_score"], "%")
    print("Recommendation:", analysis_result["recommendation"])


def main():
    """
    Main function that controls the program flow.
    """

    resume_text = """
    I am learning Python, FastAPI, REST API development, LLM applications,
    prompt engineering, RAG, embeddings, vector databases, Git, Docker,
    LangChain, AI Agents and PostgreSQL.
    I am also learning Streamlit for building simple AI demos.
    I want to build AI applications using APIs and real-world documents.
    """
    resume_text2 = """
    I am learning Python, Git.
    I am new to AI applications.
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
        "Streamlit"
    ]

    analysis_result = analyze_resume(resume_text2, required_skills)
    display_report(analysis_result)


if __name__ == "__main__":
    main()