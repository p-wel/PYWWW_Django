# Generated by Django 3.2.7 on 2021-12-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_example_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts/images/%Y/%m/%d'),
        ),
    ]
