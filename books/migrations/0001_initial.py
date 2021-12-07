# Generated by Django 3.2.7 on 2021-12-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('publication_year', models.DateField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]