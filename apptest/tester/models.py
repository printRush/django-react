from django.db import models


# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

