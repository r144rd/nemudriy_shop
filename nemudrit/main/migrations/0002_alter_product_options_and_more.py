# Generated by Django 5.1.4 on 2024-12-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='main_produc_id_f4bffc_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='main_produc_name_168fc5_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='main_produc_created_4330ad_idx'),
        ),
    ]
