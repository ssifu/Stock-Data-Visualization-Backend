# Generated by Django 4.2.5 on 2023-09-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('trade_code', models.CharField(max_length=255)),
                ('high', models.CharField(max_length=10)),
                ('low', models.CharField(max_length=10)),
                ('open', models.CharField(max_length=10)),
                ('close', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=20)),
            ],
        ),
    ]