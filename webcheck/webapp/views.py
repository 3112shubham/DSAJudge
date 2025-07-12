from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import StudentProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestCaseForm

from .forms import DSAQuestionForm, TestCaseForm
from .models import Question, TestCase
from django.contrib.auth.decorators import user_passes_test
from .models import Question, TestCase

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='admin_login')
def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})


@user_passes_test(is_admin, login_url='admin_login')
def add_question(request):
    if request.method == 'POST':
        form = DSAQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('add_testcase', question_id=question.id)
    else:
        form = DSAQuestionForm()
    return render(request, 'add_question.html', {'form': form})

def add_testcase(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            testcase = form.save(commit=False)
            testcase.question = question
            testcase.save()
            return redirect('add_testcase', question_id=question.id)
    else:
        form = TestCaseForm()  # <-- this was missing in else block

    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'add_testcase.html', context)



def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        college_name = request.POST.get('college_name')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = full_name
        user.save()

        StudentProfile.objects.create(user=user, college_name=college_name)

        return redirect('login')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Incorrect credentials.'})

    return render(request, 'login.html')



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_user(request):
    logout(request)
    return redirect('login')



@user_passes_test(is_admin, login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials.')
    return render(request, 'admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

