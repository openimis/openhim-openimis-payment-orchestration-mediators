# Generated by Django 2.2 on 2022-02-02 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainconfigs', '0002_auto_20220123_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='configs',
            name='has_port',
            field=models.BooleanField(default=False, verbose_name='Has Port Number?'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='mediator_port',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mediator Port'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='mediator_url',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="Valid URL:'https://abc.com; or http://abc.com:8000'", regex='https?:\\/\\/(?:w{1,3}\\.)?[^\\s.]+(?:\\.[a-z]+)*(?::\\d+)?(?![^<]*(?:<\\/\\w+>|\\/?>))')], verbose_name='Mediator URL'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='mifos_port',
            field=models.IntegerField(blank=True, null=True, verbose_name='Port'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='mifos_url',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="Valid URL:'https://abc.com; or http://abc.com:8000'", regex='https?:\\/\\/(?:w{1,3}\\.)?[^\\s.]+(?:\\.[a-z]+)*(?::\\d+)?(?![^<]*(?:<\\/\\w+>|\\/?>))')], verbose_name='MiFOS URL'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openhim_port',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message="Valid URL:'https://abc.com; or http://abc.com:8000'", regex='https?:\\/\\/(?:w{1,3}\\.)?[^\\s.]+(?:\\.[a-z]+)*(?::\\d+)?(?![^<]*(?:<\\/\\w+>|\\/?>))')], verbose_name='API Port'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openhim_url',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="Valid URL:'https://abc.com; or http://abc.com:8000'", regex='https?:\\/\\/(?:w{1,3}\\.)?[^\\s.]+(?:\\.[a-z]+)*(?::\\d+)?(?![^<]*(?:<\\/\\w+>|\\/?>))')], verbose_name='OpenHIM URL'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openimis_port',
            field=models.IntegerField(blank=True, null=True, verbose_name='Port'),
        ),
        migrations.AlterField(
            model_name='configs',
            name='openimis_url',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="Valid URL:'https://abc.com; or http://abc.com:8000'", regex='https?:\\/\\/(?:w{1,3}\\.)?[^\\s.]+(?:\\.[a-z]+)*(?::\\d+)?(?![^<]*(?:<\\/\\w+>|\\/?>))')], verbose_name='OpenIMIS URL'),
        ),
    ]
