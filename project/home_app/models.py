from django.db import models
from django.urls import reverse

class URL_Box(models.Model):
    id=models.AutoField(primary_key=True)
    URL=models.TextField(null=False,blank=False)

    def __str__(self):
        return f"URL {str(self.id)}"