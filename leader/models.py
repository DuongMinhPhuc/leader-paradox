from django.db import models
from django.utils import timezone

class Member(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name