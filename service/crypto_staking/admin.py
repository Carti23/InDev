from django.contrib import admin
from .models import CryptoUser, Wallet, UserPosition, StakingPool, PoolConditions


admin.site.register(CryptoUser)
admin.site.register(Wallet)
admin.site.register(UserPosition)
admin.site.register(StakingPool)
admin.site.register(PoolConditions)