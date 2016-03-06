#from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
        #글쓴이 = models.ForeignKey('auth.User')
        #제목 = models.CharField(max_length=200)
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title