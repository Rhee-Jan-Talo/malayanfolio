# Generated by Django 4.2 on 2023-05-15 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_documents_folder_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='folder_type',
        ),
    ]
