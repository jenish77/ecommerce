# Generated by Django 4.0.3 on 2022-07-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
