# Generated by Django 4.0.2 on 2022-02-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Languages_Known',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Native_Language',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='State',
            field=models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=255, null=True),
        ),
    ]