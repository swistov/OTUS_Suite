# Generated by Django 2.2.2 on 2019-06-11 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_curse_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='curse',
        ),
    ]