# Generated by Django 4.1.7 on 2023-02-21 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-published",)},
        ),
    ]
