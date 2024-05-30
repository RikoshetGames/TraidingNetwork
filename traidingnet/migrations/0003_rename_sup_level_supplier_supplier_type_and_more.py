# Generated by Django 5.0.6 on 2024-05-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traidingnet', '0002_alter_supplier_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='sup_level',
            new_name='supplier_type',
        ),
        migrations.AddField(
            model_name='supplier',
            name='supply_level',
            field=models.PositiveIntegerField(default=0, verbose_name='Уровень поставки'),
            preserve_default=False,
        ),
    ]