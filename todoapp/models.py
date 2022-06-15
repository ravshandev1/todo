from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

STATUS = (
    (0, 'New'),
    (1, 'Process'),
    (2, 'Completed'),
    (3, 'Canceled'),
)


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
