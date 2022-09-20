# Generated by Django 4.1 on 2022-09-20 12:58

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_order_alter_item_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Заказ", "verbose_name_plural": "Заказы"},
        ),
        migrations.AlterField(
            model_name="order",
            name="order",
            field=models.JSONField(
                default=dict,
                validators=[
                    main.validators.JSONSchemaValidator(
                        limit_value={
                            "properties": {
                                "amount": {"type": "number"},
                                "id": {"type": "number"},
                            },
                            "required": ["id", "amount"],
                            "type": "object",
                        }
                    )
                ],
            ),
        ),
    ]