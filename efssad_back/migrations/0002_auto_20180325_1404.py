# Generated by Django 2.0.2 on 2018-03-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efssad_back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionID', models.IntegerField()),
                ('planID', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('team', models.CharField(max_length=1000)),
                ('action', models.CharField(max_length=1000)),
                ('actiontime', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='assignedcommander',
            name='deploymentStatus',
        ),
        migrations.RemoveField(
            model_name='messagelog',
            name='planID',
        ),
        migrations.AddField(
            model_name='commander',
            name='is_deployed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignedcommander',
            name='missionID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messagelog',
            name='missionID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='commander',
            field=models.CharField(max_length=100),
        ),
    ]
