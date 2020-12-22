# Generated by Django 3.0 on 2020-09-30 23:05

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0002_auto_20200929_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enablecenter',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='enablecenter',
            name='business_hours',
            field=models.CharField(max_length=200, verbose_name='Horario de atención'),
        ),
        migrations.AlterField(
            model_name='enablecenter',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, verbose_name='Ubicación en mapa'),
        ),
        migrations.AlterField(
            model_name='enablecenter',
            name='mail',
            field=models.CharField(max_length=200, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='enablecenter',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre del centro'),
        ),
        migrations.AlterField(
            model_name='enablecenter',
            name='phone_num',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]