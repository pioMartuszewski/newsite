# Generated by Django 2.1.5 on 2019-02-14 08:41

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20190208_0927'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='booklend',
            managers=[
                ('lends', django.db.models.manager.Manager()),
            ],
        ),
    ]
