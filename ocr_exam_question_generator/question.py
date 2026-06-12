class Question:
    """Represents a single OCR-style exam question."""

    def __init__(self, question_id, level, topic, difficulty, question, marks, answer):
        self.question_id = question_id
        self.level = level
        self.topic = topic
        self.difficulty = difficulty
        self.question = question
        self.marks = marks
        self.answer = answer

    def format_for_paper(self, number):
        """Return the question formatted for a student paper."""
        return (
            f"Q{number}. [{self.topic} - {self.difficulty}]\n"
            f"{self.question}\n"
            f"({self.marks} marks)\n"
        )

    def format_for_answer_sheet(self, number):
        """Return the question and answer formatted for a teacher answer sheet."""
        return (
            f"Q{number}. {self.question}\n"
            f"Answer: {self.answer}\n"
            f"Marks: {self.marks}\n"
        )
