from django.db import models
from django.conf import settings

# Create your models here.
class Form(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Форма')
    form_link = models.CharField(max_length=255, unique=True)
    json_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    TYPE_CHOICES = (
        ('text', 'Текстовый'),
        ('lot_answer', 'С множеством ответов'),
        ('one_answer', 'С одним ответом'),
    )

    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    title_question = models.CharField(max_length=100, default='Вопрос')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.form} - {self.title_question}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    title_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.title_answer