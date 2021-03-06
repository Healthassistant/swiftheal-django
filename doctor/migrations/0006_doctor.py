# Generated by Django 3.2 on 2021-05-12 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('doctor', '0005_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Doctor_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=12)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('Aadhaar_ID', models.CharField(max_length=12)),
                ('Mobile_No', models.CharField(max_length=12)),
                ('Email', models.TextField()),
                ('Reg_No_MCI', models.CharField(max_length=10)),
                ('Qualification', models.TextField()),
                ('Area_of_Specialisation', models.CharField(max_length=30)),
                ('Year_of_Experience', models.IntegerField()),
                ('Type_of_Practice', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=50)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='doctor_profile')),
                ('Hospital_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
    ]
