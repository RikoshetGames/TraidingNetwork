# Generated by Django 5.0.6 on 2024-05-31 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traidingnet', '0006_rename_supplier_type_supplier_seller_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['seller_name'], 'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='company_name',
            new_name='seller_name',
        ),
    ]
