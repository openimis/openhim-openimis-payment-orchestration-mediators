# Generated by Django 2.2 on 2022-04-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Client ID')),
                ('externalID', models.CharField(max_length=45)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Organization Info',
                'verbose_name_plural': 'Organization Details',
                'db_table': 'client_organization',
                'ordering': ('id', 'fullname'),
                'managed': True,
            },
        ),
    ]
