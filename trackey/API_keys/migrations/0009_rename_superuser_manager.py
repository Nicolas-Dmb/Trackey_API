# Generated by Django 5.0.2 on 2024-03-10 11:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0008_alter_privatekey_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SuperUser",
            new_name="Manager",
        ),
    ]