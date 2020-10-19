from django.db import models
from django.utils import timezone
from serviceapply.models import Service
import RecruitHelper.settings as settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=50)
    like = models.IntegerField(default=0)
    work_hardness = models.IntegerField(default=5)
    work_happyness = models.IntegerField(default=5)
    work_env = models.IntegerField(default=5)
    night_work_frequency = models.IntegerField(default=5)
    self_dev = models.IntegerField(default=5)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
