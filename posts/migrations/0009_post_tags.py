# Generated by Django 3.2.7 on 2022-01-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('posts', '0008_auto_20211209_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='tags.Tag'),
        ),
    ]
