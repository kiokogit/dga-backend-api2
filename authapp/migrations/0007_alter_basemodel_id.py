# Generated by Django 3.2.7 on 2022-10-29 13:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20221029_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6921d59d-ad9e-44db-a105-5711ebb7713b'), primary_key=True, serialize=False),
        ),
    ]