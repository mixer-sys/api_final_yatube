# Generated by Django 3.2.16 on 2023-07-09 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id', 'author'), 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
