# Generated by Django 5.0.2 on 2024-03-10 16:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0012_superuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SuperUser",
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["firstname"]},
        ),
    ]
