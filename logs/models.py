from django.db import models

class Log(models.Model):
    method = models.CharField(max_length=10)
    endpoint = models.CharField(max_length=200)
    code_status = models.IntegerField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)