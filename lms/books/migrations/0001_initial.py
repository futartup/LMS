# Generated by Django 3.2.9 on 2021-12-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author_name', models.CharField(max_length=60)),
                ('isbn_num', models.CharField(max_length=60)),
                ('genre', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
    ]
