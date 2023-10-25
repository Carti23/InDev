from rest_framework import viewsets
from .models import Wallet, CryptoUser, UserPosition, StakingPool, PoolConditions
from .permissions import IsOwnerOrReadOnly, IsWalletAndUserPositionOwner
from rest_framework.permissions import IsAuthenticated
from .serializers import WalletSerializer, CryptoUserSerializer, UserPositionSerializer, StakingPoolSerializer, PoolConditionsSerializer


class UserPositionViewSet(viewsets.ModelViewSet):
    queryset = UserPosition.objects.all()
    serializer_class = UserPositionSerializer
    permission_classes = [IsAuthenticated, IsWalletAndUserPositionOwner]


class CryptoUserViewSet(viewsets.ModelViewSet):
    queryset = CryptoUser.objects.all()
    serializer_class = CryptoUserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated, IsWalletAndUserPositionOwner]


class StakingPoolViewSet(viewsets.ModelViewSet):
    queryset = StakingPool.objects.all()
    serializer_class = StakingPoolSerializer
    permission_classes = [IsAuthenticated]


class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer
    permission_classes = [IsAuthenticated]
