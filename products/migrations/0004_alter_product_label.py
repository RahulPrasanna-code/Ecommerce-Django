# Generated by Django 4.0.4 on 2022-06-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category_product_label_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('best-seller', 'primary'), ('trusted', 'secondary'), ('NEW', 'danger')], max_length=20),
        ),
    ]
