from django.db import models

# Create your models here.
class publication(models.Model): 
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title 
             