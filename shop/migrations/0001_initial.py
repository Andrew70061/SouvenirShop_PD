import django.core.validators
import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Индекс')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.CharField(choices=[('1_cart', 'cart'), ('2_waiting_for_payment', 'waiting_for_payment'), ('3_paid', 'paid')], default='1_cart', max_length=32)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('site', models.URLField(blank=True, verbose_name='Сайт')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, verbose_name='Примечание')),
                ('markup', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Наценка')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('sku', models.CharField(max_length=255, verbose_name='Артикул')),
                ('barcode', models.CharField(blank=True, max_length=255, verbose_name='Штрихкод')),
                ('manufacturer', models.CharField(blank=True, max_length=255, verbose_name='Компания-производитель')),
                ('manufacturer_countries', models.CharField(blank=True, max_length=255, verbose_name='Страна-производитель')),
                ('vendor', models.CharField(blank=True, max_length=255, verbose_name='Производитель')),
                ('vendor_code', models.CharField(blank=True, max_length=255, verbose_name='Артикул производителя')),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Длина (см.)')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ширина (см.)')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Высота (см.)')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Вес (г.)')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена со скидкой')),
                ('quantity', models.IntegerField(default=0, null=True, verbose_name='Количество товара')),
                ('supplier_sku', models.IntegerField(default=0, null=True, verbose_name='Артикул у поставщика')),
                ('supplier_url', models.URLField(blank=True, verbose_name='URL')),
                ('supplier_price', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена у поставщика')),
                ('supplier_quantity', models.IntegerField(default=0, null=True, verbose_name='Количество товара у поставщика')),
                ('ozon_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='OZON ID')),
                ('wb_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Wildberries ID')),
                ('yandex_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Яндекс ID')),
                ('vk_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='VK ID')),
                ('publish', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Цена со скидкой')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='slug')),
                ('ozon_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='OZON ID')),
                ('wb_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Wildberries ID')),
                ('yandex_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Яндекс ID')),
                ('vk_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='VK ID')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.productcategory', verbose_name='Родительская категория')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.productcategory', verbose_name='Категория товара'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/uploads/images/%Y/%m', verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, max_length=255, verbose_name='Атрибут alt')),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Порядок сортировки')),
                ('supplier_url', models.URLField(blank=True, verbose_name='URL')),
                ('vk_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='VK ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.supplier', verbose_name='Поставщик'),
        ),
    ]
