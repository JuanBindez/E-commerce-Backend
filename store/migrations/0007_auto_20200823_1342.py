# Generated by Django 3.0.7 on 2020-08-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200823_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(max_length=200),
        ),
    ]
