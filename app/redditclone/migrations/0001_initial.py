# Generated by Django 2.0.4 on 2018-09-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('body', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]