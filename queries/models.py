from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    timestamp = models.DateTimeField(default=now)
    hashtag = models.CharField(max_length=100, default='public')
    question_p = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like_question')
    comment_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'Question'
        ordering = ['-timestamp']

    def __str__(self):
        return f"From User: {self.user} - Question ID: {self.id} - Text: {self.text[:50]}..."


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=now)

    class Meta:
        db_table = 'Comment'
        ordering = ['-timestamp']

    def __str__(self):
        return f"From User: {self.user} - Comment: {self.timestamp}"


