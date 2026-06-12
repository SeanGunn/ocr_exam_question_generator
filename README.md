# OCR Exam Question Generator

A Python command-line application that generates OCR-style Computer Science practice question sets.

This project is designed as a small portfolio project showing:
- Python programming
- Object-oriented design
- JSON data handling
- Random question selection
- File output
- Basic command-line interaction

## Features

- Generate OCR-style Computer Science question papers
- Choose GCSE or A Level mode
- Choose number of questions
- Randomised question selection
- Generates a student question paper
- Generates a teacher answer sheet
- Saves outputs as `.txt` files
- Question bank stored separately in JSON for easy editing

## How to Run

```bash
python main.py
```

## Example Use

1. Select qualification level:
   - GCSE
   - A Level

2. Enter number of questions.

3. The program creates:
   - `generated_paper.txt`
   - `answer_sheet.txt`

## Project Structure

```text
ocr_exam_question_generator/
│
├── main.py
├── question_generator.py
├── question.py
├── questions.json
└── README.md
```

## Possible Future Improvements

- Export to PDF or Word document
- Add topic filtering
- Add difficulty filtering
- Add mark scheme formatting
- Add GUI using Tkinter
- Add web interface using Flask
