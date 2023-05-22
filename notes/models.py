from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # auto_now_add=True sets the date and time to the current date and time when the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete=models.CASCADE deletes all the notes of the user when the user is deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")
