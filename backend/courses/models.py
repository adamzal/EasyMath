from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class DuoMathCourse(models.Model):

    class SchoolType(models.TextChoices):
        PRIMARY_SCHOOL = "PS", _('Primary School')
        SECONDARY_SCHOOL = "SS", _('Secondary School')

    class LevelType(models.TextChoices):
        BASIC = "B", _('Basic')
        ADVANCE = "A", _('Advance')

    course_name = models.CharField(max_length=100, default="Course name")
    type_of_school = models.CharField(max_length=2, choices=SchoolType.choices, default=SchoolType.PRIMARY_SCHOOL)
    type_of_level = models.CharField(max_length=1, choices=LevelType.choices, default=LevelType.BASIC)

    def __str__(self):
        return f"{self.id} - {self.type_of_school} - {self.type_of_level}"


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50, default="Chapter name")
    chapter_number = models.PositiveIntegerField(default=0)
    course = models.ForeignKey(DuoMathCourse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.chapter_name}"


class Lesson(models.Model):
    lesson_topic = models.CharField(max_length=50, default="Lesson topic")
    lesson_number = models.PositiveIntegerField(default=0)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} - {self.lesson_topic}"


class Exercise(models.Model):

    class ExerciseDifficult(models.TextChoices):
        EASY = "E", _("Easy")
        MID = "M", _("Mid")
        HARD = "H", _("Hard")

    exercise_number = models.PositiveIntegerField(default=0)
    function_name = models.CharField(max_length=13, default="PPPCH00L00E00")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    difficult = models.CharField(max_length=1, choices=ExerciseDifficult.choices, default=ExerciseDifficult.EASY)
    text = models.CharField(max_length=300, default="Text")
    answear = models.CharField(max_length=300, default="Answear")
    points = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} - {self.function_name} - {self.points}"
