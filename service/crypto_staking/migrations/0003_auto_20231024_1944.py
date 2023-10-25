# Generated by Django 3.2.16 on 2023-10-24 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crypto_staking', '0002_auto_20231024_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='StakingPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='poolconditions',
            name='max_stake_amount',
        ),
        migrations.RemoveField(
            model_name='poolconditions',
            name='min_stake_amount',
        ),
        migrations.RemoveField(
            model_name='poolconditions',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='userposition',
            name='amount_staked',
        ),
        migrations.RemoveField(
            model_name='userposition',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='private_key',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='public_key',
        ),
        migrations.AddField(
            model_name='poolconditions',
            name='min_stake',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userposition',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userposition',
            name='coin_symbol',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wallet',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.user'),
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='CryptoUser',
        ),
        migrations.DeleteModel(
            name='StackingPool',
        ),
        migrations.AddField(
            model_name='stakingpool',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='staking_pools', to='crypto_staking.CryptoUser'),
        ),
        migrations.AddField(
            model_name='poolconditions',
            name='staking_pool',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crypto_staking.stakingpool'),
            preserve_default=False,
        ),
    ]
