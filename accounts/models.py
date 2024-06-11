from django.db import models
from django.contrib.auth.models import User
class UserPic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/user/%Y/%m/%d/')

    class Meta:
        db_table="userpictures"


    def __str__(self):
        return str(self.user)