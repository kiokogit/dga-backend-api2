# Generated by Django 4.1.3 on 2023-02-15 10:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packages_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecurrencymodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='packageimagesmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='packagemodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='packageremarks',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='packagereviewsmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tagsmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4903866-b54a-4c02-ab22-41bf46b4be62'), editable=False, primary_key=True, serialize=False),
        ),
    ]
