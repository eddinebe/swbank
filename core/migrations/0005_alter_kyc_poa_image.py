# Generated by Django 5.0.1 on 2024-02-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_kyc_poa_image_alter_kyc_poi_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kyc",
            name="poa_image",
            field=models.ImageField(upload_to="kyc/poa/"),
        ),
    ]
