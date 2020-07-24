from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class Application(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.TextField()
    attached_file = models.FileField(default='defaultFile.png', upload_to='attached_files')
    date_applied = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver1 = models.EmailField(max_length=100)
    receiver2 = models.EmailField(max_length=100)
    done = models.BooleanField(default=False)
    def attatched_file_link(self):
        if self.attached_file:
            return (self.attached_file.url)
        else:
            return "No attachment"

    def __str__(self):
        return self.title


class Permission(models.Model):
    parent = models.ForeignKey(Application, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    phase = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.parent.title

