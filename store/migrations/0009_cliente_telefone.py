# Generated by Django 3.0.7 on 2020-08-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_cliente_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]