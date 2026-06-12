from question_generator import QuestionGenerator


def get_number_input(prompt, minimum, maximum):
    """Get a valid integer from the user within a set range."""
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a number between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("OCR Exam Question Generator")
    print("=" * 30)

    generator = QuestionGenerator()

    if not generator.questions:
        print("No questions could be loaded.")
        return

    levels = generator.get_available_levels()

    print("\nAvailable levels:")
    for index, level in enumerate(levels, start=1):
        print(f"{index}. {level}")

    level_choice = get_number_input(
        "\nSelect a level: ",
        1,
        len(levels)
    )

    selected_level = levels[level_choice - 1]
    available_questions = generator.filter_questions(selected_level)

    print(f"\nThere are {len(available_questions)} questions available for {selected_level}.")

    number_of_questions = get_number_input(
        "How many questions would you like to generate? ",
        1,
        len(available_questions)
    )

    paper = generator.generate_paper(selected_level, number_of_questions)

    generator.save_paper(paper)
    generator.save_answer_sheet(paper)

    print("\nQuestion paper generated successfully.")
    print("Files created:")
    print("- generated_paper.txt")
    print("- answer_sheet.txt")


if __name__ == "__main__":
    main()
