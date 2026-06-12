import json
import random
from question import Question


class QuestionGenerator:
    """Loads questions and generates random OCR-style exam papers."""

    def __init__(self, question_file="questions.json"):
        self.question_file = question_file
        self.questions = self.load_questions()

    def load_questions(self):
        """Load questions from a JSON file and convert them into Question objects."""
        try:
            with open(self.question_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: Could not find {self.question_file}")
            return []
        except json.JSONDecodeError:
            print(f"Error: {self.question_file} is not valid JSON.")
            return []

        questions = []
        for item in data:
            questions.append(
                Question(
                    item["id"],
                    item["level"],
                    item["topic"],
                    item["difficulty"],
                    item["question"],
                    item["marks"],
                    item["answer"]
                )
            )

        return questions

    def get_available_levels(self):
        """Return all qualification levels in the question bank."""
        return sorted(set(question.level for question in self.questions))

    def filter_questions(self, level):
        """Return questions matching the selected qualification level."""
        return [
            question for question in self.questions
            if question.level.lower() == level.lower()
        ]

    def generate_paper(self, level, number_of_questions):
        """Generate a random exam paper for the selected level."""
        matching_questions = self.filter_questions(level)

        if not matching_questions:
            return []

        if number_of_questions > len(matching_questions):
            number_of_questions = len(matching_questions)

        return random.sample(matching_questions, number_of_questions)

    def save_paper(self, selected_questions, filename="generated_paper.txt"):
        """Save the student version of the question paper."""
        total_marks = sum(question.marks for question in selected_questions)

        with open(filename, "w", encoding="utf-8") as file:
            file.write("OCR Computer Science Practice Paper\n")
            file.write("=" * 35 + "\n\n")
            file.write(f"Total Marks: {total_marks}\n\n")

            for index, question in enumerate(selected_questions, start=1):
                file.write(question.format_for_paper(index))
                file.write("\n")

    def save_answer_sheet(self, selected_questions, filename="answer_sheet.txt"):
        """Save the teacher answer sheet."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write("OCR Computer Science Answer Sheet\n")
            file.write("=" * 35 + "\n\n")

            for index, question in enumerate(selected_questions, start=1):
                file.write(question.format_for_answer_sheet(index))
                file.write("\n")
