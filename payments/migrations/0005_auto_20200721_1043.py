# Generated by Django 3.0.4 on 2020-07-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reference',
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]
