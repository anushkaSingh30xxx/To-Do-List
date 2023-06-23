from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#determines what rows and tables we have in our database
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #connects two modules,if user got deleted from database, all the todo items he created also gets deleted
    todo_name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name
