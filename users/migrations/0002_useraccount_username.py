# Generated by Django 3.0.5 on 2023-10-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='username',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
    ]
