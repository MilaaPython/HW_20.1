# Generated by Django 4.2.1 on 2023-05-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='наименование')),
                ('product_description', models.TextField(verbose_name='описание')),
                ('product_preview', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('product_category', models.CharField(max_length=100, verbose_name='категория')),
                ('product_cost', models.FloatField(verbose_name='цена')),
                ('product_data_created', models.DateField(verbose_name='создан')),
                ('product_last_data_change', models.DateField(verbose_name='последнее изменение')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('product_name',),
            },
        ),
    ]
