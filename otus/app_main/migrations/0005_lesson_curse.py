# Generated by Django 2.2.2 on 2019-06-11 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_remove_lesson_curse'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='curse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_main.Curse'),
            preserve_default=False,
        ),
    ]
