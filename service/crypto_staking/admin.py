from django.contrib import admin
from .models import CryptoUser, Wallet, UserPosition, StakingPool, PoolConditions


# Define custom admin classes for each model
class CryptoUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'wallet_address')
    list_filter = ('user',)


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')
    list_filter = ('owner__user',)


class UserPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'coin_symbol', 'amount')
    list_filter = ('owner__user', 'coin_symbol')


class StakingPoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)


class PoolConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'staking_pool', 'min_stake', 'annual_interest_rate')
    list_filter = ('staking_pool__name', 'min_stake')


# Register the models with their custom admin classes
admin.site.register(CryptoUser, CryptoUserAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(UserPosition, UserPositionAdmin)
admin.site.register(StakingPool, StakingPoolAdmin)
admin.site.register(PoolConditions, PoolConditionsAdmin)
