# Generated by Django 2.0.2 on 2018-03-24 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commander',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('name', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_mainComm', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssignedCommander',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploymentStatus', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('planID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionID', models.IntegerField()),
                ('level', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('datetimeReceived', models.DateTimeField()),
                ('datetimeCompleted', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=1000)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('commander', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='messagelog',
            name='missionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efssad_back.Mission'),
        ),
        migrations.AddField(
            model_name='assignedcommander',
            name='missionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efssad_back.Mission'),
        ),
        migrations.AddField(
            model_name='assignedcommander',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
