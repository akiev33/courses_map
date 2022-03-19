from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey("news.News", on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} -> {self.news}'
