# Generated by Django 3.2 on 2023-11-21 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Имя пользователя содержит недопустимый символ!', regex='^[\\w.@+-]+$'), django.core.validators.RegexValidator(message='Использовать имя "me" запрещено!', regex='me')], verbose_name='Имя пользователя'),
        ),
    ]
