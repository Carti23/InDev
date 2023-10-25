from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserPositionViewSet, CryptoUserViewSet, WalletViewSet, StakingPoolViewSet, PoolConditionsViewSet


# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'user-positions', UserPositionViewSet, basename='user-position')
router.register(r'crypto-users', CryptoUserViewSet, basename='crypto-user')
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'staking-pools', StakingPoolViewSet, basename='staking-pools')
router.register(r'pool-condition', PoolConditionsViewSet, basename='pool-condition')

urlpatterns = [
    path('', include(router.urls)),
]
