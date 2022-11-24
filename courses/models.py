from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=150)
    month = models.IntegerField(default=3)
    day = models.IntegerField(default=3)
    price = models.IntegerField(default=0)
    desc = models.TextField()

    slug=models.SlugField(blank=True,null=True,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()

    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Aply(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    phone=models.CharField(max_length=100)
    q_phone=models.CharField(max_length=100)
    kusr=models.TextField()

    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Course)
def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug=slugify(instance.title)




# def article_post_save(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.slug = slugify(instance.title)
#         instance.save()
