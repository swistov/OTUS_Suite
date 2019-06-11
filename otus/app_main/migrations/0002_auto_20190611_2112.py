# Generated by Django 2.2.2 on 2019-06-11 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curse',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.TextField()),
                ('enabled', models.BooleanField()),
                ('curse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.Curse')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
