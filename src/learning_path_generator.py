def generate_learning_path(user_skills, recommended_career, df):
    """
    Generate missing skills, step-by-step weekly learning plan
    and career-based certificates.

    Returns:
        missing_skills (list)
        learning_plan (list of dict)
        certificates (list)
    """

    # ---------------- Career → Certificates Mapping ----------------
    CAREER_CERTIFICATES = {
        "technology": [
            "Google IT Support Professional Certificate",
            "IBM IT Fundamentals",
            "CompTIA ITF+"
        ],
        "data": [
            "Google Data Analytics Certificate",
            "IBM Data Science Professional Certificate"
        ],
        "design": [
            "Google UX Design Certificate",
            "UI/UX Design – Coursera"
        ],
        "security": [
            "Google Cybersecurity Certificate",
            "CompTIA Security+"
        ],
        "web": [
            "Meta Front-End Developer Certificate",
            "Responsive Web Design – freeCodeCamp"
        ],
        "ui": [
            "Google UX Design Certificate",
            "Figma UI/UX Essentials"
        ],
        "web apps": [
            "Meta Full Stack Developer Certificate",
            "Django & React Full Stack"
        ],
        "ai": [
            "IBM AI Engineering Certificate",
            "Deep Learning – Andrew Ng"
        ],
        "cloud": [
            "AWS Cloud Practitioner",
            "Microsoft Azure Fundamentals"
        ],
        "automation": [
            "Google IT Automation with Python",
            "UiPath RPA Developer"
        ]
    }

    # ---------------- Fetch Career Row ----------------
    career_row = df[df["career"] == recommended_career.lower()]

    if career_row.empty:
        return [], [], []

    required_skills = [
        s.strip().lower()
        for s in career_row.iloc[0]["skills"].split(",")
    ]

    # ---------------- Missing Skills Logic (IMPORTANT FIX) ----------------
    user_skills = [s.lower().strip() for s in user_skills]

    missing_skills = [
        skill for skill in required_skills
        if skill not in user_skills
    ]

    # ---------------- Weekly Learning Plan ----------------
    learning_plan = []

    for i, skill in enumerate(missing_skills):
        learning_plan.append({
            "week": f"Week {i + 1}",
            "skill": skill.title(),
            "time": "6–8 hours",
            "tasks": [
                f"Learn basics of {skill}",
                f"Practice hands-on exercises",
                f"Build 1 mini project using {skill}"
            ]
        })

    # ---------------- Certificates ----------------
    certificates = CAREER_CERTIFICATES.get(
        recommended_career.lower(), []
    )

    return missing_skills, learning_plan, certificates
