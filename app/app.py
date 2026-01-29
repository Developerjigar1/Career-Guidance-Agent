from src.data_load import load_data
from src.text_preprocessing import clean_text
from src.career_recommender import recommend_career
from src.learning_path_generator import generate_learning_path


def main():
    print("Welcome to Career Guidance Agent\n")

    df = load_data("data/row_data/career_dataset.csv")
    if df is None:
        return

    df["career"] = df["career"].str.strip().str.lower()
    df["skills"] = df["skills"].str.strip().str.lower()
    df["interest"] = df["interest"].str.strip().str.lower()

    user_skills_input = input("Enter your skills (comma separated): ")
    user_interest_input = input("Enter your interests: ")

    user_skills = [s.strip().lower() for s in user_skills_input.split(",")]
    user_profile = clean_text(user_skills_input + " " + user_interest_input)

    career = recommend_career(user_profile, df)
    print(f"\nRecommended Career: {career.title()}")

    missing_skills, learning_path = generate_learning_path(
        user_skills, career, df
    )

    if missing_skills:
        print("\nSkills to Learn:")
        for s in missing_skills:
            print("-", s)

        print("\nLearning Path:")
        for step in learning_path:
            print(step)
    else:
        print("\nYou already have all required skills!")


if __name__ == "__main__":
    main()
