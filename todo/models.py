from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    priorty = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'
