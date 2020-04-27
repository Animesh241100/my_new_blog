from django.db import models
from django.urls import reverse

class Article(models.Model):
    title   = models.CharField(("Enter title"), max_length=100)
    content = models.TextField(blank=False, null=True)
    active  = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("Blog_app:article-detail", kwargs={"my_id": self.id})
    
