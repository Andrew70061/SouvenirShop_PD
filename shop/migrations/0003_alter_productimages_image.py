from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m', verbose_name='Изображение'),
        ),
    ]
