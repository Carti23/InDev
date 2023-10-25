from rest_framework import serializers
from .models import Wallet, CryptoUser, UserPosition, StakingPool, PoolConditions


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class CryptoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoUser
        fields = ('id', 'user', 'wallet_address')

    def validate_walletaddress(self, wallet_address):
        # Validate that the wallet_address is not negative
        if wallet_address < 0:
            raise serializers.ValidationError(
                "wallet_address cannot be negative")
        return wallet_address


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = ('id', 'owner', 'coin_symbol', 'amount')

    def validate_amount(self, amount):
        # Validate that the amount is not negative
        if amount < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        return amount


class StakingPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakingPool
        fields = ('id', 'name', 'description', 'participants')


class PoolConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolConditions
        fields = ('id', 'staking_pool', 'min_stake', 'annual_interest_rate')
