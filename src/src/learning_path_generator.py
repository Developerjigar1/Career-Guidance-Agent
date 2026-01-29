def generate_learning_path(user_skills, recommended_career, df):
    career_row = df[df["career"] == recommended_career]

    if career_row.empty:
        return [], []

    required_skills = career_row.iloc[0]["skills"].split(",")

    # only missing skills
    missing_skills = [
        skill.strip()
        for skill in required_skills
        if skill.strip() not in user_skills
    ]

    return missing_skills, []   # 👈 SAFE return (2 values only)
