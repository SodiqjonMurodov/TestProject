# Generated by Django 5.1.1 on 2024-10-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]
