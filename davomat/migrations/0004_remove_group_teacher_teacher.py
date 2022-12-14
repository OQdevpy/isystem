# Generated by Django 4.1.1 on 2022-10-27 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('davomat', '0003_remove_davomat_pupil_davomat_pupils_davomat_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(to='davomat.group')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
