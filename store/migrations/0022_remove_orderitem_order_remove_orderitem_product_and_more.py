# Generated by Django 4.2.1 on 2023-06-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_product_subcategory_alter_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Category/Industry'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('category',), 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
