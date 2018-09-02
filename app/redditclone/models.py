from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        _title = self.title
        return _title[:30]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        _body = self.body
        return _body[:30]
