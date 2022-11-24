# Generated by Django 4.1.1 on 2022-10-27 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('davomat', '0002_remove_davomat_dates_remove_teacher_course_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='davomat',
            name='pupil',
        ),
        migrations.AddField(
            model_name='davomat',
            name='pupils',
            field=models.ManyToManyField(to='davomat.pupil'),
        ),
        migrations.AddField(
            model_name='davomat',
            name='teacher',
            field=models.CharField(default='salom', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
