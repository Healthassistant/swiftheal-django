# Generated by Django 3.2 on 2021-05-03 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0002_alter_doctor_reg_no_mci"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="doctor",
            table="Doctor",
        ),
    ]