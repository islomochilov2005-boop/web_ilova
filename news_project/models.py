from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=512)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/', null=True, blank=True)
    video = models.FileField(upload_to='news/videos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ["-published_at"]
        verbose_name_plural = "news"
        verbose_name = 'news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
