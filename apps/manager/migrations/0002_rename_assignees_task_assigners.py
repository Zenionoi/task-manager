# Generated by Django 4.1.7 on 2023-05-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="assignees", new_name="assigners",
        ),
    ]