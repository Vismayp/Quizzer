# -*- coding: utf-8 -*-
import csv
from quiz.models import Question

def import_questions_from_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    question, created = Question.objects.get_or_create(
                        question_text=row['question_text'],
                        defaults={
                            'difficulty': row['difficulty'],
                            'option1': row['option1'],
                            'option2': row['option2'],
                            'option3': row['option3'],
                            'option4': row['option4'],
                            'correct_option': row['correct_option'],
                        }
                    )
                    if created:
                        print(f"Added question: {row['question_text']}")
                    else:
                        print(f"Question already exists: {row['question_text']}")
                except Exception as e:
                    print(f"Error adding question: {row}. Error: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Call the function
import_questions_from_csv('questions.csv')
# python manage.py shell
# exec(open('push_questions.py').read())