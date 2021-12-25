from django.db import models

# Create your models here.

# class Folder(models.Model):
#     label = models.CharField(max_length=60)

#     def __str__(self):
#         return self.content

class Thought(models.Model):
    content = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.content

