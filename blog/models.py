from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import date


class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email_address = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    date = models.DateField(editable=False)
    slug = models.CharField(max_length=50, unique=True)
    text = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(2000)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.id:
            self.date = date.today()
        return super(Post, self).save(*args, **kwargs)
