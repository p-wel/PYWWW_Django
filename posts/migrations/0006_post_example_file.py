# Generated by Django 3.2.7 on 2021-12-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='example_file',
            field=models.FileField(blank=True, null=True, upload_to='posts/esamples'),
        ),
    ]
