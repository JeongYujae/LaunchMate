from django.db import models

class User(models.Model):
    usernmae=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usernmae

