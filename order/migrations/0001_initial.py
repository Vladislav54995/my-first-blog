# Generated by Django 5.0.9 on 2024-11-10 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(default='87010000000', max_length=100, verbose_name='номер телефона')),
                ('total', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100)),
                ('Person_name', models.CharField(max_length=50)),
                ('Expiry', models.CharField(max_length=50)),
                ('cvv', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]