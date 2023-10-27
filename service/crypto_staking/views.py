from rest_framework import viewsets
from .models import Wallet, CryptoUser, UserPosition, StakingPool, PoolConditions
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from web3 import Web3
from rest_framework import status
from rest_framework import filters
import os
from .serializers import WalletSerializer, CryptoUserSerializer, UserPositionSerializer, StakingPoolSerializer, PoolConditionsSerializer


class UserPositionViewSet(viewsets.ModelViewSet):
    queryset = UserPosition.objects.all()
    serializer_class = UserPositionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['coin_symbol']


class CryptoUserViewSet(viewsets.ModelViewSet):
    queryset = CryptoUser.objects.all()
    serializer_class = CryptoUserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['wallet_address']


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    # Retrieve the Infura URL from environment variables
    infura_url = os.getenv('INFURA_URL')

    def get_wallet_balance(self, wallet_address):
        # Initialize a Web3 instance with the Infura API URL
        web3 = Web3(Web3.HTTPProvider(self.infura_url))

        try:
            # Use Web3 to get the wallet balance
            balance_wei = web3.eth.get_balance(wallet_address)
            balance_eth = web3.from_wei(balance_wei, 'ether')

            return {
                'balance': balance_eth,
                'wallet_address': wallet_address
            }
        except Exception as e:
            return None

    def retrieve(self, request, *args, **kwargs):
        # Retrieve the wallet associated with the currently authenticated user
        wallet = get_object_or_404(CryptoUser, user=request.user)
        wallet_address = wallet.wallet_address
        print(wallet_address)

        # Get the wallet balance using the Web3 API
        wallet_data = self.get_wallet_balance(wallet_address)

        if wallet_data is not None:
            # Return the wallet data with a success status
            return Response(wallet_data, status=status.HTTP_200_OK)
        else:
            # Return an error response if the balance cannot be fetched
            return Response({"error": "Failed to fetch wallet balance"}, status=status.HTTP_400_BAD_REQUEST)


class StakingPoolViewSet(viewsets.ModelViewSet):
    queryset = StakingPool.objects.all()
    serializer_class = StakingPoolSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['min_stake', 'annual_interest_rate']
