# Generated by Django 3.2.3 on 2021-05-25 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.PositiveIntegerField(default=160)),
                ('male', models.BooleanField(default=False)),
                ('website', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(default='不願意透漏身份的人', max_length=10)),
                ('message', models.TextField()),
                ('del_pass', models.CharField(max_length=10)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.mood')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('budget', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('note', models.TextField()),
                ('ddate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
