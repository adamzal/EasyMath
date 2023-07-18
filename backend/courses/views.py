from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import DuoMathCourse
from users.models import DuoMathUser, UserCourse, UserChapter, UserLesson, UserExercise
# Create your views here.

def show_courses(request):
    if request.user.is_authenticated:
        user_courses = UserCourse.objects.filter(user=request.user)
        return render(request, 'courses/index.html', {'courses': user_courses})
    else:
        return render(request, 'users/login.html')
    return render(request, 'duomath/index.html')

def show_chapters(request, name, user_course_pk):
    if request.user.is_authenticated:
        user_course = UserCourse.objects.get(pk=user_course_pk)
        user_chapters = UserChapter.objects.filter(user_course=user_course)
        return render(request, 'courses/index.html', {'chapters': user_chapters})
    else:
        return render(request, 'users/login.html')
    return render(request, 'duomath/index.html')

def show_lessons(request, name, user_chapter_pk):
    if request.user.is_authenticated:
        user_chapter = UserChapter.objects.get(pk=user_chapter_pk)
        user_lessons = UserLesson.objects.filter(user_chapter=user_chapter)
        return render(request, 'courses/index.html', {'lessons': user_lessons})
    else:
        return render(request, 'users/login.html')
    return render(request, 'duomath/index.html')

def show_all_courses(request):
    if request.user.is_authenticated:
        courses = DuoMathCourse.objects.all()
        return render(request, 'courses/index.html', {'all_courses': courses})
    return render(request, 'duomath/index.html')

def add_new_course(request, name, course_pk):
    if request.user.is_authenticated:
        user_course = UserCourse.objects.filter(user=request.user, course__pk=course_pk)
        if not user_course:

            course = DuoMathCourse.objects.get(pk=course_pk)

            new_user_course = UserCourse(user=request.user, course=course)
            new_user_course.save()

            return render(request, 'courses/index.html')
        else:
            return render(request, 'courses/index.html')
    else:
        return render(request, 'users/login.html')
    return render(request, 'duomath/index.html')


def do_lesson(request, name, user_lesson_pk):
    if request.user.is_authenticated:
        user_lesson = UserLesson.objects.get(pk=user_lesson_pk)
        user_exercises = UserExercise.objects.filter(user_lesson=user_lesson)
        print(user_lesson, user_lesson_pk)
        print(user_exercises)
        return render(request, 'courses/index.html', {'exercises': user_exercises})
    else:
        return render(request, 'users/login.html')
    return render(request, 'duomath/index.html')


