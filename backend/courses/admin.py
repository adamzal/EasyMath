from django.contrib import admin
from .models import DuoMathCourse, Chapter, Lesson, Exercise
# Register your models here.

admin.site.register(DuoMathCourse)
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(Exercise)