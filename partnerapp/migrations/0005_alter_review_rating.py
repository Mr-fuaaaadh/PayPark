# Generated by Django 5.1.5 on 2025-01-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0004_alter_payment_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(),
        ),
    ]
