# Generated by Django 5.2.4 on 2025-07-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestapp', '0004_remove_requesting_tutor_session_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesting_tutor',
            name='counter_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requesting_tutor',
            name='counter_proposed_rate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requesting_tutor',
            name='counter_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requesting_tutor',
            name='counter_time_from',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requesting_tutor',
            name='counter_time_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
