from django.db import models

from django.db import models
from django.contrib.auth.models import User
class TaskUsers(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    dead_line=models.DateField(null=True,blank=True)
    do=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    alarm_d=models.DateField(blank=True,null=True)
    alarm_t=models.TimeField(blank=True,null=True)

    class Meta:
        db_table="Tasks"


    def __str__(self):
        return f"{self.title}  {self.user}"
    

class Projects(models.Model):
    title=models.CharField(max_length=100)
    tasks=models.ManyToManyField(TaskUsers)
    created_time=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dead_line=models.DateField(null=True,blank=True)
    do=models.BooleanField(default=True)

    class Meta:
        db_table="Projects"

        
    def __str__(self):
        return f"{self.title} {self.user}"
