from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=140)
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

