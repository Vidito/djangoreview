from django.db import models
from django.urls import reverse
from datetime import date, datetime
# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100, default=None)
    text = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='poems_images/')

    def get_absolute_url(self):
        return reverse('poem_detail', kwargs = {'id': self.id}) 

    def __str__(self):
        return self.title
