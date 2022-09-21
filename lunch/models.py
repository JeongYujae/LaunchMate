from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime 

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Appointment(BaseModel):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='my_appointment',on_delete=models.CASCADE) #충돌이 일어나서 related_name으로 migrations에서 충돌 피할 수 있음
    participate_user_set=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    title=models.CharField(max_length=30, help_text='약속 제목')
    date=models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("jstagram:post_detail", kwargs={"pk": self.pk}``)
    


class Menu(BaseModel):
    MENU_CHOICES=(
    ('KOREAN','한식'),
    ('JAPANESE','일식'),
    ('CHINESE','중식'),
    ('ITALIAN','양식'),
    ('SNACK','분식')
)
    suggestion=models.CharField(max_length=10, choices=MENU_CHOICES)
    