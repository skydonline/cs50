# Generated by Django 4.2.3 on 2023-07-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_listing_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="for_sale",
            field=models.BooleanField(default=True),
        ),
    ]
