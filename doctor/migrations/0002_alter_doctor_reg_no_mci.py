# Generated by Django 3.2 on 2021-05-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="Reg_No_MCI",
            field=models.CharField(max_length=10),
        ),
    ]
