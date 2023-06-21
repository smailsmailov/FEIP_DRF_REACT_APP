# Generated by Django 4.2.1 on 2023-06-21 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='id_o',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.order_list'),
        ),
        migrations.AlterField(
            model_name='order_list',
            name='type_of_delivery',
            field=models.CharField(choices=[('2', 'Доставка'), ('1', 'Самовывоз')], default='1', max_length=2),
        ),
    ]
