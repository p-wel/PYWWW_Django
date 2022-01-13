# Generated by Django 3.2.7 on 2022-01-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(related_name='categories', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Opublikowany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sponsored',
            field=models.BooleanField(default=False, verbose_name='Sponsorowany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Tytuł'),
        ),
    ]
