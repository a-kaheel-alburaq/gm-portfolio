# Generated by Django 5.1.3 on 2025-05-22 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_productcategory_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('filter_class', models.CharField(help_text='CSS class used for filtering (e.g., filter-beef-premium)', max_length=50)),
                ('order', models.IntegerField(default=0, help_text='Order in which the subcategory appears')),
                ('is_active', models.BooleanField(default=True)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='home.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Product Sub Categories',
                'ordering': ['parent_category', 'order'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='home.productsubcategory'),
        ),
    ]
