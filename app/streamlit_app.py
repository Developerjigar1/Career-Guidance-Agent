import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Career Guidance Agent",
    page_icon="🎯",
    layout="wide"
)

# ---------------- DATA (SIMPLE HARD CODED) ----------------
CAREER_DATA = {
    "technology": {
        "skills": ["python", "java", "git", "problem solving"],
        "certificates": [
            "Python for Everybody – Coursera",
            "Java Programming – Udemy",
            "Git & GitHub – Google"
        ]
    },
    "data": {
        "skills": ["python", "sql", "excel", "power bi"],
        "certificates": [
            "Google Data Analytics – Coursera",
            "SQL for Data Analysis – Udemy",
            "Microsoft Power BI – Microsoft"
        ]
    },
    "design": {
        "skills": ["figma", "ui/ux", "adobe xd", "prototyping"],
        "certificates": [
            "Google UX Design – Coursera",
            "Figma Masterclass – Udemy",
            "Adobe XD Course – Adobe"
        ]
    },
    "security": {
        "skills": ["networking", "cryptography", "ethical hacking", "linux"],
        "certificates": [
            "CompTIA Security+ – CompTIA",
            "Ethical Hacking – Udemy",
            "CISSP Fundamentals – ISC2"
        ]
    },
    "web": {
        "skills": ["html", "css", "javascript", "react"],
        "certificates": [
            "Meta Front-End Developer – Coursera",
            "JavaScript Bootcamp – Udemy",
            "React – Meta"
        ]
    },
    "ui": {
        "skills": ["ui design", "typography", "color theory", "figma"],
        "certificates": [
            "UI Design Essentials – Coursera",
            "Figma Masterclass – Udemy",
            "Adobe XD Masterclass – Adobe"
        ]
    },
    "web apps": {
        "skills": ["javascript", "react", "node.js", "databases"],
        "certificates": [
            "Full Stack Web Developer – Coursera",
            "MERN Stack Developer – Udemy",
            "Web Development Bootcamp – Udemy"
        ]
    },
    "ai": {
        "skills": ["python", "machine learning", "deep learning"],
        "certificates": [
            "AI For Everyone – Coursera",
            "Machine Learning – Andrew Ng",
            "Deep Learning Specialization"
        ]
    },
    "cloud": {
        "skills": ["aws", "azure", "docker", "kubernetes"],
        "certificates": [
            "AWS Certified Solutions Architect – AWS",
            "Microsoft Azure Fundamentals – Microsoft",
            "Docker & Kubernetes – Udemy"
        ]
    },
    "automation": {
        "skills": ["python", "scripting", "testing", "ci/cd"],
        "certificates": [
            "Python for Automation – Coursera",
            "Test Automation – Udemy",
            "CI/CD Pipeline – Linux Academy"
        ]
    }
}

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center;'>🎯 Career Guidance Agent</h1>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("🧑‍🎓 Your Profile")

user_skills_input = st.sidebar.text_area(
    "Your Skills (comma separated)",
    placeholder="python, sql"
)

user_interest = st.sidebar.selectbox(
    "Your Interest",
    ["Technology", "Data", "Design", "Security", "Web", "UI", "Web Apps", "AI", "Cloud", "Automation"]
)

submit = st.sidebar.button("🚀 Recommend Career")

# ---------------- LOGIC ----------------
if submit:
    user_skills = [s.strip().lower() for s in user_skills_input.split(",") if s.strip()]
    career_key = user_interest.lower()

    st.success(f"🎯 Recommended Career: **{user_interest}**")

    required_skills = CAREER_DATA[career_key]["skills"]
    certificates = CAREER_DATA[career_key]["certificates"]

    # missing skills
    missing_skills = [s for s in required_skills if s not in user_skills]

    # ---------------- PROGRESS ----------------
    total = len(required_skills)
    done = total - len(missing_skills)
    progress = int((done / total) * 100)

    st.markdown("### 📈 Career Readiness")
    st.progress(progress)
    st.caption(f"You are **{progress}% ready**")

    # ---------------- SKILLS ----------------
    if missing_skills:
        st.markdown("### 🛠 Skills to Learn (Step-by-Step)")

        for i, skill in enumerate(missing_skills, start=1):
            st.markdown(
                f"""
                <div style="padding:15px;border-left:6px solid #2196F3;background:#eef6ff;margin-bottom:10px;">
                <h4>📅 Week {i}: {skill.title()}</h4>
                <ul>
                    <li>Learn basics</li>
                    <li>Practice examples</li>
                    <li>Build mini project</li>
                </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.balloons()
        st.success("🎉 You already have all required skills!")

    # ---------------- CERTIFICATES ----------------
    st.markdown("### 📜 Recommended Certificates")

    for cert in certificates:
        st.markdown(
            f"""
            <div style="padding:10px;border-left:6px solid #4CAF50;background:#f9f9f9;margin-bottom:8px;">
            🎓 {cert}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- MARKET TREND & FUTURE SCOPE ----------------
    st.markdown("### 📊 Market Trend & Future Scope")

    CAREER_MARKET = {
        "technology": {
            "trend": "High demand in web & mobile applications, cloud development.",
            "future": "Jobs expected to grow ~25% by 2030 with rising tech adoption.",
            "roadmap": [
                "Learn core language (Python/Java)",
                "Data Structures & Algorithms",
                "Web frameworks (Django/React)",
                "Version control (Git/GitHub)",
                "Build real projects",
                "Deploy apps on cloud"
            ]
        },
        "data": {
            "trend": "High demand for data-driven decision making across industries.",
            "future": "Data jobs growing ~30% with Big Data & AI adoption.",
            "roadmap": [
                "Learn Python basics",
                "Master SQL",
                "Learn Excel & data visualization",
                "Learn Power BI/Tableau",
                "Practice analysis projects",
                "Learn statistics & machine learning basics"
            ]
        },
        "design": {
            "trend": "Growing demand for UX/UI designers in digital transformation.",
            "future": "Design jobs growing ~20% with emphasis on user experience.",
            "roadmap": [
                "Master design principles",
                "Learn Figma or Adobe XD",
                "Understand user research",
                "Build portfolio with case studies",
                "Learn prototyping & wireframing",
                "Understand responsive design"
            ]
        },
        "security": {
            "trend": "Critical demand for cybersecurity professionals globally.",
            "future": "Security jobs growing ~33% due to increasing cyber threats.",
            "roadmap": [
                "Learn networking fundamentals",
                "Master Linux & command line",
                "Study cryptography basics",
                "Learn ethical hacking",
                "Get security certifications",
                "Practice on CTF platforms"
            ]
        },
        "web": {
            "trend": "Consistent demand for responsive websites & web apps.",
            "future": "Web dev jobs stable with large freelance & full-time demand.",
            "roadmap": [
                "Learn HTML, CSS",
                "Master JavaScript",
                "Learn React or Angular",
                "Build portfolio projects",
                "Understand backend basics",
                "Deploy sites on hosting"
            ]
        },
        "ui": {
            "trend": "High demand for UI designers in digital products and apps.",
            "future": "UI design jobs growing ~25% with focus on user interfaces.",
            "roadmap": [
                "Learn design fundamentals",
                "Master Figma",
                "Study typography & color theory",
                "Learn prototyping tools",
                "Build component libraries",
                "Create design systems"
            ]
        },
        "web apps": {
            "trend": "Soaring demand for full-stack web app developers.",
            "future": "Web app development jobs growing ~28% with SaaS expansion.",
            "roadmap": [
                "Learn frontend (HTML/CSS/JavaScript)",
                "Master React or Vue",
                "Learn backend (Node.js/Python)",
                "Master databases (SQL/NoSQL)",
                "Learn APIs & REST",
                "Deploy full applications"
            ]
        },
        "ai": {
            "trend": "AI & ML roles skyrocketing with automation and analytics.",
            "future": "AI job growth ~35%+, especially in research & products.",
            "roadmap": [
                "Python basics",
                "Machine Learning fundamentals",
                "Deep Learning with TensorFlow/PyTorch",
                "Build AI models",
                "Participate in Kaggle competitions"
            ]
        },
        "cloud": {
            "trend": "Massive demand for cloud architects and engineers.",
            "future": "Cloud jobs growing ~32% with enterprise migration.",
            "roadmap": [
                "Learn cloud fundamentals",
                "Master AWS or Azure",
                "Learn containerization (Docker)",
                "Study Kubernetes orchestration",
                "Learn infrastructure as code",
                "Design scalable systems"
            ]
        },
        "automation": {
            "trend": "High demand for automation engineers across industries.",
            "future": "Automation jobs growing ~25% with digital transformation.",
            "roadmap": [
                "Learn Python scripting",
                "Master test automation frameworks",
                "Learn CI/CD pipelines",
                "Study DevOps practices",
                "Learn infrastructure automation",
                "Build automation projects"
            ]
        }
    }

    market_info = CAREER_MARKET.get(career_key.lower(), None)

    if market_info:
        st.markdown(f"**📈 Current Market Trend:** {market_info['trend']}")
        st.markdown(f"**🔮 Future Scope:** {market_info['future']}")
        
        st.markdown("### 🧠 Structured Learning Roadmap")
        for idx, step in enumerate(market_info["roadmap"], start=1):
            st.write(f"👉 Step {idx}: {step}")
    else:
        st.info("Market trend & roadmap info not available for this career.")


# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
