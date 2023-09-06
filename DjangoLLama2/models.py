from django.db import models

class LLamaQA(models.Model):
    question = models.CharField(max_length=10000000)
    answer = models.TextField()
