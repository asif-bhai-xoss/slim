from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from book_control.models import BookModel
from user_control.forms import *
from user_control.models import *
from .decorators import *


@unauthenticated_user
def home(request):
    return render(request, 'index.html')


@unauthenticated_user
def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_student:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('student-dashboard')
            elif user and user.is_publisher:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('publisher-dashboard')
            else:
                messages.error(request, 'Email or Password is incorrect.')
                return redirect('login')
        else:
            return render(request, 'login.html', {'form': form})

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


@unauthenticated_user
def student_register_view(request):
    if request.method == 'POST':
        student_reg_form = StudentRegistrationForm(request.POST)
        if student_reg_form.is_valid():
            student_reg_form.save()
            email = student_reg_form.cleaned_data.get('email')
            raw_password = student_reg_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            StudentProfileModel.objects.create(user=user)
            login(request, user)
            return redirect('student-dashboard')
        else:
            return render(request, 'student/student-registration.html', {"student_reg_form": student_reg_form})

    student_reg_form = StudentRegistrationForm()
    context = {
        "student_reg_form": student_reg_form
    }
    return render(request, 'student/student-registration.html', context)


@unauthenticated_user
def publisher_register_view(request):
    if request.method == 'POST':
        publisher_reg_form = PublisherRegistrationForm(request.POST)
        if publisher_reg_form.is_valid():
            publisher_reg_form.save()
            email = publisher_reg_form.cleaned_data.get('email')
            raw_password = publisher_reg_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            PublisherProfileModel.objects.create(user=user)
            login(request, user)
            return redirect('publisher-dashboard')
        else:
            return render(request, 'publisher/publisher-registration.html', {"publisher_reg_form": publisher_reg_form})

    publisher_reg_form = PublisherRegistrationForm()
    context = {
        "publisher_reg_form": publisher_reg_form
    }
    return render(request, 'publisher/publisher-registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def student_dashboard_view(request):
    return render(request, 'student/student-dashboard.html')


@login_required
def publisher_dashboard_view(request):
    books = BookModel.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'publisher/publisher-dashboard.html', context)


@login_required
def student_profile_view(request, pk):
    user = User.objects.get(id=pk)
    student = StudentProfileModel.objects.get(user=user)

    context = {
        'user': user,
        'student': student
    }
    return render(request, 'student/student-profile.html', context)
