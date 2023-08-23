# Generated by Django 4.2.4 on 2023-08-23 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_registro',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='tu@email.com', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=100),
        ),
    ]