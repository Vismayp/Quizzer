from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question
import random

def home(request):
    return render(request, 'quiz/home.html')

def quiz_setup(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        num_questions = int(request.POST.get('num_questions'))
        timer = int(request.POST.get('timer'))

        # Fetch questions based on level
        questions = list(Question.objects.filter(difficulty=level).order_by('?')[:num_questions])
        
        request.session['questions'] = [q.id for q in questions]
        request.session['timer'] = timer
        return redirect('start_quiz')
    
    return render(request, 'quiz/setup.html')

def start_quiz(request):
    question_ids = request.session.get('questions', [])
    timer = request.session.get('timer', 0)
    questions = Question.objects.filter(id__in=question_ids)

    return render(request, 'quiz/quiz.html', {'questions': questions, 'timer': timer})

def result(request):
    if request.method == 'POST':
        correct_count = 0
        questions = Question.objects.filter(id__in=request.session.get('questions', []))
        for question in questions:
            selected_option = int(request.POST.get(str(question.id), 0))
            if selected_option == question.correct_option:
                correct_count += 1

        return render(request, 'quiz/result.html', {
            'total': len(questions),
            'correct': correct_count,
        })
    return redirect('home')
