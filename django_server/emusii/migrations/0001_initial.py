# Generated by Django 3.1.4 on 2021-01-08 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='node',
            fields=[
                ('song_id', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('channel', models.CharField(max_length=120)),
                ('E', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='E_nav', to='emusii.node')),
                ('N', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='N_nav', to='emusii.node')),
                ('W', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='W_nav', to='emusii.node')),
                ('_emoji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusii.emoji')),
                ('s', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='S_nav', to='emusii.node')),
            ],
        ),
    ]
