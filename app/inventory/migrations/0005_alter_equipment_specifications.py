# Generated by Django 4.0.10 on 2024-07-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_supplier_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='specifications',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
