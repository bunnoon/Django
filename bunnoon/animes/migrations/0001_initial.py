# Generated by Django 4.2.3 on 2023-07-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, null=True)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('animePk', models.CharField(max_length=7, unique=True)),
                ('title', models.CharField(max_length=60)),
                ('enName', models.CharField(max_length=60)),
                ('thName', models.CharField(max_length=60)),
            ],
        ),
    ]
