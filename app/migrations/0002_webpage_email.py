# Generated by Django 4.2.7 on 2023-12-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(max_length=254, null=2),
            preserve_default=2,
        ),
    ]
