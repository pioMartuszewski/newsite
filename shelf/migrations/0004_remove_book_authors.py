# Generated by Django 2.1.5 on 2019-02-07 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_author_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
    ]
