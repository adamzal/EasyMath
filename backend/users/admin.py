from django.contrib import admin
from .models import DuoMathUser, UserCourse, UserChapter, UserLesson, UserExercise
# Register your models here.

admin.site.register(DuoMathUser)
admin.site.register(UserCourse)
admin.site.register(UserChapter)
admin.site.register(UserLesson)
admin.site.register(UserExercise)
