from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Exam, Quiz, User
import traceback

from .serialization import Serializationclass
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    try:
        exam_detail = Exam.objects.all()
        if request.method == 'POST':
            email = request.POST['email']
            exam_name = request.POST['exam_name']
            exam_id = Exam.objects.filter(name=exam_name).first()
            user_detail = User.objects.filter(email=email, exam_id=exam_id.id)
            if len(user_detail) == 0:
                return redirect('quiz',exam_id.id, email)
            else:
                score =user_detail.values_list('score')[0][0]
                return redirect('dashboard', score)
        else:   
            return render(request, 'quizapp/start_page.html',{'exam_detail': exam_detail})
    except Exception as e:
        traceback.print_exc()
        return redirect('index')


def quiz(request, id, email):
    quiz_detail = Quiz.objects.filter(exam_detail=id)
    if request.method == "POST":
        user_response = dict(request.POST)
        correct_response = {}
        for i in quiz_detail:
            correct_response[i.id] = i.correct_ans
        correct_ans = 0
        total_que = len(correct_response.keys())
        for i in correct_response:
            if correct_response[i] == user_response[str(i)][0]:
                correct_ans = correct_ans + 1
        score = (correct_ans / total_que)*100
        exam = Exam.objects.filter(id=id).first()
        user = User.objects.create(email=email, score=score, exam_id_id=id)
        user.save()
        return redirect('dashboard', score)
    else:
        return render(request, 'quizapp/quiz.html',{'quiz_detail': quiz_detail})

def dashboard(request , score):
    return render(request, 'quizapp/dashboard.html', {'score': score})


@api_view(['GET'])
def showuser(request, exam_id=None):
    if request.method == 'GET':
        results = User.objects.filter(exam_id_id=exam_id)
        serializer = Serializationclass(results, many=True)
        return Response(serializer.data)