# Generated by Django 3.1.2 on 2021-01-15 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_tbl_return'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_return',
            name='return_cat',
        ),
    ]
