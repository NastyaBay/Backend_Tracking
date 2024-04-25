from django.db import models
from django.conf import settings

# Create your models here.
class Form(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Форма')
    form_link = models.URLField(blank=True)
    qr_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    title_question = models.CharField(max_length=100, default='Вопрос')

    def __str__(self):
        return self.title_question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title_answer = models.CharField(max_length=255)
    sum_answer = models.IntegerField(default=0)

    def __str__(self):
        return self.title_answer