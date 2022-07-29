# Generated by Django 4.0.6 on 2022-07-29 17:21

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugs", "0002_add_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Severity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("weight", models.IntegerField(default=0)),
                ("icon", models.CharField(max_length=64)),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=18, samples=None
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Severity",
            },
        ),
        migrations.AddField(
            model_name="bug",
            name="severity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.CASCADE,
                to="bugs.severity",
            ),
        ),
    ]
