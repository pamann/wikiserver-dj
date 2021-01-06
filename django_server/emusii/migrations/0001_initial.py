# Generated by Django 3.1.4 on 2021-01-06 14:28

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('channel', models.CharField(max_length=120)),
                ('_emoji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusii.emoji')),
                ('nav_options', models.ManyToManyField(related_name='_node_nav_options_+', to='emusii.node')),
            ],
        ),
        migrations.CreateModel(
            name='graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emusii.node')),
            ],
        ),
        migrations.CreateModel(
            name='activesubgraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active', to='emusii.node')),
                ('nodes', models.ManyToManyField(to='emusii.node')),
            ],
        ),
    ]
