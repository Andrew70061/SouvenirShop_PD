from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Новый заказ', 'new'), ('Сборка заказа', 'processing'), ('Доставляется или готов к выдаче', 'completed'), ('Отменен', 'cancelled')], default='Новый заказ', max_length=32),
        ),
    ]
