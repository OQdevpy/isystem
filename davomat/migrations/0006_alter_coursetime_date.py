# Generated by Django 4.1.2 on 2022-10-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davomat', '0005_group_course_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetime',
            name='date',
            field=models.CharField(choices=[('1', 'Du/Chor/Juma'), ('2', 'Se/Pay/Sha')], max_length=30),
        ),
    ]