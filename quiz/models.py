from django.db import models

class Question(models.Model):
    DIFFICULTY_LEVELS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    question_text = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()  # Store 1, 2, 3, or 4 for the correct option

    def __str__(self):
        return self.question_text


