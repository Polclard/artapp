# Generated by Django 5.1.5 on 2025-01-27 14:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("artexhebitionapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exhibition",
            name="art",
        ),
    ]
