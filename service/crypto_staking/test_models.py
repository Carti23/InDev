from django.test import TestCase
from django.contrib.auth.models import User
from .models import CryptoUser, Wallet, UserPosition, StakingPool, PoolConditions


# Test cases for CryptoUser model
class CryptoUserModelTest(TestCase):
    def test_crypto_user_creation(self):
        # Test creating a CryptoUser and check its attributes
        user = User.objects.create_user(
            username="testuser", password="testpassword")
        crypto_user = CryptoUser.objects.create(
            user=user, wallet_address="test_wallet_address")
        self.assertEqual(crypto_user.user, user)  # Check user association
        self.assertEqual(crypto_user.wallet_address,
                         "test_wallet_address")  # Check wallet address


# Test cases for Wallet model
class WalletModelTest(TestCase):
    def test_wallet_creation(self):
        # Test creating a Wallet and check its owner
        user = User.objects.create_user(
            username="testuser", password="testpassword")
        crypto_user = CryptoUser.objects.create(
            user=user, wallet_address="test_wallet_address")
        wallet = Wallet.objects.create(owner=crypto_user)
        # Check wallet owner association
        self.assertEqual(wallet.owner, crypto_user)


# Test cases for UserPosition model
class UserPositionModelTest(TestCase):
    def test_user_position_creation(self):
        # Test creating a UserPosition and check its attributes
        user = User.objects.create_user(
            username="testuser", password="testpassword")
        crypto_user = CryptoUser.objects.create(
            user=user, wallet_address="test_wallet_address")
        user_position = UserPosition.objects.create(
            owner=crypto_user, coin_symbol="BTC", amount=10.5)
        # Check owner association
        self.assertEqual(user_position.owner, crypto_user)
        self.assertEqual(user_position.coin_symbol, "BTC")  # Check coin symbol
        self.assertEqual(user_position.amount, 10.5)  # Check amount


# Test cases for StakingPool model
class StakingPoolModelTest(TestCase):
    def test_staking_pool_creation(self):
        # Test creating a StakingPool and check its attributes
        staking_pool = StakingPool.objects.create(
            name="Pool 1", description="Test staking pool")
        self.assertEqual(staking_pool.name, "Pool 1")  # Check name
        self.assertEqual(staking_pool.description,
                         "Test staking pool")  # Check description

    def test_staking_pool_participants(self):
        # Test adding participants to a StakingPool and check the count
        user1 = User.objects.create_user(
            username="user1", password="password1")
        crypto_user1 = CryptoUser.objects.create(
            user=user1, wallet_address="wallet1")
        user2 = User.objects.create_user(
            username="user2", password="password2")
        crypto_user2 = CryptoUser.objects.create(
            user=user2, wallet_address="wallet2")
        staking_pool = StakingPool.objects.create(
            name="Pool 1", description="Test staking pool")
        staking_pool.participants.add(crypto_user1, crypto_user2)
        # Check the count of participants
        self.assertEqual(staking_pool.participants.count(), 2)


# Test cases for PoolConditions model
class PoolConditionsModelTest(TestCase):
    def test_pool_conditions_creation(self):
        # Test creating PoolConditions and check its attributes
        staking_pool = StakingPool.objects.create(
            name="Pool 1", description="Test staking pool")
        pool_conditions = PoolConditions.objects.create(
            staking_pool=staking_pool, min_stake=100.0, annual_interest_rate=5.0)
        # Check staking pool association
        self.assertEqual(pool_conditions.staking_pool, staking_pool)
        self.assertEqual(pool_conditions.min_stake,
                         100.0)  # Check minimum stake
        self.assertEqual(pool_conditions.annual_interest_rate,
                         5.0)  # Check annual interest rate
