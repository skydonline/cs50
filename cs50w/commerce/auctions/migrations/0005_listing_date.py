# Generated by Django 4.2.3 on 2023-07-15 22:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_listing_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
