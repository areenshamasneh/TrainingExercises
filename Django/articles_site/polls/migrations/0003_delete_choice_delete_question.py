# Generated by Django 5.0.7 on 2024-07-17 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
