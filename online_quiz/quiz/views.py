# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})

def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    score = 0

    for question in questions:
        selected_choice = request.POST.get(str(question.id))
        if selected_choice:
            choice = question.choices.get(id=selected_choice)
            if choice.is_correct:
                score += 1

    return render(request, 'quiz/quiz_result.html', {'quiz': quiz, 'score': score})
    
