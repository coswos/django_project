# Generated by Django 4.2.6 on 2023-11-10 20:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_email"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Issue",
        ),
    ]
