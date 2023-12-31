# Generated by Django 4.2.1 on 2023-05-30 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0018_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField()),
                ('paid_amount', models.IntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_intent', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.order')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category/Industry'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('watingapproval', 'Wating approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.product'),
        ),
    ]
