# Generated by Django 4.1.3 on 2023-01-07 06:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packages_service', '0004_packagemodel_package_id_alter_basemodel_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagelocationmodel',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='packagelocationmodel',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packagerelatedevent',
            name='basemodelwithstatus_ptr',
        ),
        migrations.RemoveField(
            model_name='packagerelatedevent',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packagetimelinesmodel',
            name='basemodelwithstatus_ptr',
        ),
        migrations.RemoveField(
            model_name='packagetimelinesmodel',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packagecurrencymodel',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packageimagesmodel',
            name='package',
        ),
        migrations.RemoveField(
            model_name='packageimagesmodel',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='packagereviewsmodel',
            name='package',
        ),
        migrations.AddField(
            model_name='packagecurrencymodel',
            name='package_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packageimagesmodel',
            name='package_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='city_town',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='county',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='event_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='event_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='event_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='no_of_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='no_of_nights',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='package_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='package_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='packagereviewsmodel',
            name='package_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='packagemodel',
            name='package_id',
            field=models.UUIDField(default=uuid.UUID('c24d00a8-5338-441b-802f-6293b5676e67'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='packagemodel',
            unique_together={('reference_number', 'package_id')},
        ),
        migrations.DeleteModel(
            name='PackageAnalytics',
        ),
        migrations.DeleteModel(
            name='PackageLocationModel',
        ),
        migrations.DeleteModel(
            name='PackageRelatedEvent',
        ),
        migrations.DeleteModel(
            name='PackageTimelinesModel',
        ),
    ]