# Generated by Django 3.2.16 on 2023-10-24 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StackingPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_name', models.CharField(max_length=255)),
                ('pool_address', models.CharField(max_length=255)),
                ('token_name', models.CharField(max_length=255)),
                ('staking_duration', models.PositiveIntegerField()),
                ('total_staked', models.DecimalField(decimal_places=6, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=6, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.CharField(max_length=255)),
                ('public_key', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_staked', models.DecimalField(decimal_places=6, max_digits=20)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.stackingpool')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.user')),
            ],
        ),
        migrations.CreateModel(
            name='PoolConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_stake_amount', models.DecimalField(decimal_places=6, max_digits=20)),
                ('max_stake_amount', models.DecimalField(decimal_places=6, max_digits=20)),
                ('annual_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.stackingpool')),
            ],
        ),
    ]
