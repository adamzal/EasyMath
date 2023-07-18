from django.urls import path
from . import views

app_name = 'courses'

urlpatterns=[
    path('', views.show_courses, name='index'),
    path('add=<int:course_pk><str:name>', views.add_new_course, name='add_new_course'),
    path('show_all_courses/', views.show_all_courses, name='show_all_courses'),
    path('course=<int:user_course_pk><str:name>/', views.show_chapters, name='show_chapters'),
    path('chapter=<int:user_chapter_pk><str:name>/', views.show_lessons, name='show_lessons'),
    path('lesson=<int:user_lesson_pk><str:name>/', views.do_lesson, name='do_lesson'),
]