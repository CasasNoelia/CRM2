# Generated by Django 3.0.5 on 2020-04-22 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_usuario_empleo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibo',
            name='user',
        ),
    ]
