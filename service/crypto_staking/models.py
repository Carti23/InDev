from django.db import models
from django.contrib.auth.models import User


class CryptoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=255)


class Wallet(models.Model):
    owner = models.OneToOneField(CryptoUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wallet of {self.owner.user.username}"

class UserPosition(models.Model):
    owner = models.ForeignKey(CryptoUser, on_delete=models.CASCADE)
    coin_symbol = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.owner.user.username}'s position in {self.coin_symbol}"

class StakingPool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(CryptoUser, related_name='staking_pools', blank=True)

    def __str__(self):
        return self.name

class PoolConditions(models.Model):
    staking_pool = models.ForeignKey(StakingPool, on_delete=models.CASCADE)
    min_stake = models.DecimalField(max_digits=10, decimal_places=2)
    annual_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Conditions for {self.staking_pool.name}"
