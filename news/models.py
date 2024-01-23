from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, null=True, blank=True)
    is_menu = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        pass
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=512)
    short_desc = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='news')
    view = models.IntegerField(default=0, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.CharField(max_length=128)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.new.title}"


class Contact(models.Model):
    ism = models.CharField(verbose_name="Ismi", max_length=128)
    phone = models.CharField(verbose_name="telefon", max_length=128)
    xabar = models.TextField(verbose_name="xabar")
    date = models.DateTimeField(auto_now_add=True)

    is_trash = models.BooleanField(default=False)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return f" Trash:{self.is_trash} |Contacted:{self.is_contacted} | User:{self.ism}"
