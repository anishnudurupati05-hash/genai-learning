"""
Day 1 Project: Resume Skill Gap Analyzer v0.1
"""

resume_text = """
I am learning Python, FastAPI, REST API development, LLM applications,
prompt engineering, RAG, embeddings, vector databases, Git, Docker,
LangChain, and PostgreSQL.
I want to build AI applications using APIs and real-world documents.
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
    "AI Agents"
]

matched_skills = []
missing_skills = []

for skill in required_skills:
    if skill.lower() in resume_text.lower():
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

match_score = (len(matched_skills) / len(required_skills)) * 100

print("===== Resume Skill Gap Analyzer v0.1 =====")
print()

print("Matched Skills:")
for skill in matched_skills:
    print("-", skill)

print()

print("Missing Skills:")
for skill in missing_skills:
    print("-", skill)

print()
print("Match Score:", round(match_score, 2), "%")
print()

if match_score >= 80:
    print("Recommendation: Strong match. Continue building portfolio projects.")
elif match_score >= 50:
    print("Recommendation: Moderate match. Improve missing technical skills.")
else:
    print("Recommendation: Beginner level. Focus on foundation skills first.")