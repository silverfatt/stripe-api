# Generated by Django 4.1.1 on 2022-09-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("order", models.JSONField()),
            ],
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
    ]
