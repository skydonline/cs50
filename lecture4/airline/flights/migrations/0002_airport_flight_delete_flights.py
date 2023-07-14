# Generated by Django 4.2.3 on 2023-07-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("airport_code", models.CharField(max_length=3)),
                ("city", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("duration", models.IntegerField()),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="arrivals",
                        to="flights.airport",
                    ),
                ),
                (
                    "origin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departures",
                        to="flights.airport",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Flights",
        ),
    ]
