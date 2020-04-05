# Generated by Django 3.0.4 on 2020-04-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
