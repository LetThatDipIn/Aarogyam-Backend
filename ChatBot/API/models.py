from django.db import models

# Create your models here.

class Chat(models.Model):
    _input = models.TextField()
    _output = models.TextField()
    
    class Meta:
        db_table = "ChatBot"