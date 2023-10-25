from rest_framework import serializers
from .models import Wallet, CryptoUser, UserPosition, StakingPool, PoolConditions


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('owner', 'balance')


class CryptoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoUser
        fields = ('id', 'user', 'wallet_address', 'balance')

    def validate_walletaddress(self, wallet_address):
        if wallet_address < 0:
            raise serializers.ValidationError(
                "wallet_address cannot be negative")
        return wallet_address


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = ('id', 'owner', 'coin_symbol', 'amount')

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        return amount


class StakingPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakingPool
        fields = ('id', 'name', 'description', 'participants')

    def validate_participants(self, participants):
        if participants < 0:
            raise serializers.ValidationError(
                "Participants cannot be negative")
        return participants


class PoolConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolConditions
        fields = ('id', 'staking_pool', 'min_stake', 'annual_interest_rate')

    def validate_min_stake(self, min_stake):
        if min_stake < 0:
            raise serializers.ValidationError(
                "Minimum stake cannot be negative")
        return min_stake

    def validate_annual_interest_rate(self, annual_interest_rate):
        if annual_interest_rate < 0:
            raise serializers.ValidationError(
                "Annual interest rate cannot be negative")
        return annual_interest_rate
