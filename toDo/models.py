from django.db import models

# Create your models here.
class toDo(models.Model):
    text = models.CharField(max_length = 200)
    added_date = models.DateTimeField(auto_now= True)
    description = models.TextField(blank = True)
    
    def __str__(self):
        return self.text
