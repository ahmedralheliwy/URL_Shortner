from django.db import models

class URL_Box(models.Model):
    id=models.PositiveBigIntegerField(primary_key=True)
    URL=models.TextField(null=False,blank=False)


    def __str__(self):
        return 'URL'.joint(id)
        