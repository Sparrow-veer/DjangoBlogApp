from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import asyncio
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    fruit_pic=models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.fruit_pic.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.fruit_pic.path)