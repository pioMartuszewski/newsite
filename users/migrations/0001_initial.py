# Generated by Django 2.1.5 on 2019-02-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('login', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
