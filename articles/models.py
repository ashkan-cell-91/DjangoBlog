from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.jpg", blank=True)
    # add in author
    def __str__(self):
        return self.title
    def snippet(self):
        #تعداد کاراکتر ها را محدود نشون میده
        return self.body[:50] + '...'
