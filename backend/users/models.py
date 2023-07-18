from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from courses.models import DuoMathCourse, Chapter, Lesson, Exercise
# Create your models here.


class DuoMathUser(AbstractUser):

    xp = models.PositiveIntegerField(default=0)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)
    hearts = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.username


class UserCourse(models.Model):
    course = models.ForeignKey(DuoMathCourse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(DuoMathUser, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.id} - {self.user.username} - {self.completed}"


class UserChapter(models.Model):
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.chapter.id} - {self.user_course.user.username} - {self.completed}"


class UserLesson(models.Model):
    user_chapter = models.ForeignKey(UserChapter, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lesson.id} - {self.user_chapter.user_course.user.username} - {self.completed}"


class UserExercise(models.Model):
    user_lesson = models.ForeignKey(UserLesson, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercise.id} - {self.user_lesson.user_chapter.user_course.user.username} - {self.completed}"


@receiver(post_save, sender=UserCourse)
def create_chapters(sender, instance, created, **kwargs):
    if created:
        for ch in Chapter.objects.filter(course=instance.course):
            new_chapter = UserChapter(pk=ch.pk, user_course=instance, chapter=ch)
            new_chapter.save()


@receiver(post_save, sender=UserChapter)
def create_lessons(sender, instance, created, **kwargs):
    if created:
        for l in Lesson.objects.filter(chapter=instance.chapter):
            new_lesson = UserLesson(pk=l.pk, user_chapter=instance, lesson=l)
            new_lesson.save()


@receiver(post_save, sender=UserLesson)
def create_exercises(sender, instance, created, **kwargs):
    if created:
        for e in Exercise.objects.filter(lesson=instance.lesson):
            new_exercise = UserExercise(pk=e.pk, user_lesson=instance, exercise=e)
            new_exercise.save()
