# Generated by Django 5.0.2 on 2024-03-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0007_alter_privatekey_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="privatekey",
            name="image",
            field=models.ImageField(upload_to="key_images/"),
        ),
    ]