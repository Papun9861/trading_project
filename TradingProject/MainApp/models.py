from django.db import models

# Create your models here.
class Csv(models.Model):
    name=models.FileField(upload_to='csvs')
    time=models.TimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)
    activated=models.BooleanField(default=False)
    
    def __str__(self) :
        return f"file id:{self.id}"
