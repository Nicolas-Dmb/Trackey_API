# Generated by Django 5.0.2 on 2024-03-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0010_remove_user_id_superuser_alter_user_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]