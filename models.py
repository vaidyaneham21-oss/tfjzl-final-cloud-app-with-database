from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def is_get_score(self, selected_ids):
        correct_choices = self.choice_set.filter(is_correct=True)
        correct_ids = set([c.id for c in correct_choices])
        return correct_ids == set(selected_ids)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)