# Generated by Django 2.2.5 on 2021-02-01 08:07

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
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('contents', models.CharField(max_length=200, verbose_name='글 내용')),
            ],
        ),
    ]
