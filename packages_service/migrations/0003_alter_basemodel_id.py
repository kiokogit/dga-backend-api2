# Generated by Django 4.1.3 on 2023-01-07 05:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packages_service', '0002_alter_basemodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4d98ec72-cc04-4063-b410-d43f751728c4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]