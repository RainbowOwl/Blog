from django.db import models
from django.conf import settings


class Tag(models.Model):
    value = models.CharField(max_length=90)

    def __str__(self):
        return self.value



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False, null=False)
    content = models.CharField(max_length=30000, blank=True)
    created = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title



class Like(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.count

    def increase_count(self):
        self.count += 1
        self.save()

    def decrease_count(self):
        self.count -= 1
        self.save()

    def clear_count(self):
        self.count = 0
        self.save()
