# Generated by Django 3.2.10 on 2022-09-19 08:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='商品名称')),
            ],
        ),
        migrations.CreateModel(
            name='ProductProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('title', models.CharField(max_length=128, verbose_name='商品名称')),
                ('description', models.CharField(max_length=128, verbose_name='商品描述')),
            ],
        ),
    ]
