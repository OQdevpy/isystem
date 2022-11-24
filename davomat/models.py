from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
course_date = (
    ('1', 'Du/Chor/Juma'),
    ('2', 'Se/Pay/Sha'),
)

course_time = (
    ('1', '11:00'),
    ('2', '13:00'),
    ('3', '15:00'),
)


class CourseTime(models.Model):
    date = models.CharField(max_length=30, choices=course_date)
    time = models.CharField(max_length=30, choices=course_time)


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    date = models.ForeignKey(CourseTime, on_delete=models.CASCADE, null=True)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Pupil(models.Model):
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_time = models.ForeignKey(CourseTime, on_delete=models.CASCADE, null=True)
    pupils = models.ManyToManyField(Pupil)


class Teacher(models.Model):
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.teacher.username


class Davomat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    teacher = models.CharField(max_length=100)
    pupils = models.ManyToManyField(Pupil)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.group.title}->{self.date.date()}'


@receiver(pre_save, sender=Davomat)
def teacher_pre_save(sender, instance, *args, **kwargs):
    instance.teacher = instance.group.teacher
