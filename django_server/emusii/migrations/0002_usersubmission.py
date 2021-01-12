# Generated by Django 3.1.4 on 2021-01-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emusii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.URLField(max_length=70)),
                ('youtube_emojis', models.CharField(max_length=120)),
                ('user_name', models.CharField(max_length=120)),
                ('user_emojis', models.CharField(max_length=120)),
            ],
        ),
    ]
