from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Новый заказ', 'Новый заказ'), ('Сборка заказа', 'Сборка заказа'), ('Доставляется или готов к выдаче', 'Доставляется или готов к выдаче'), ('Отменен', 'Отменен')], default='Новый заказ', max_length=32),
        ),
    ]
