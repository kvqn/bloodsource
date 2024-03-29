# Generated by Django 4.1.5 on 2023-04-16 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0006_auto_20230416_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyReceived',
            fields=[
                ('money_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date_of_payment', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
