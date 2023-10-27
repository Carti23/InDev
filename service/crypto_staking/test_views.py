from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .models import StakingPool, PoolConditions, Wallet
from .views import StakingPoolViewSet, PoolConditionsViewSet
from django.contrib.auth.models import User
from unittest.mock import patch
from rest_framework.test import APIClient


# Test cases for WalletViewSet
class WalletViewSetTestCase(TestCase):
    def setUp(self):
        # Set up user and client
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.client = APIClient()

    @patch('crypto_staking.views.os.getenv')
    @patch('crypto_staking.views.Web3')
    def test_retrieve_wallet_balance_success(self, mock_web3, mock_getenv):
        # Test retrieving wallet balance successfully
        mock_getenv.return_value = 'https://infura_url_here'
        web3_instance = mock_web3.return_value
        web3_instance.eth.get_balance.return_value = 1000000000000000000

        wallet = Wallet.objects.create(owner=self.user)

        response = self.client.get(f'/api/wallets/{wallet.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['wallet_address'], wallet.wallet_address)

    @patch('crypto_staking.views.os.getenv')
    @patch('crypto_staking.views.Web3')
    def test_retrieve_wallet_balance_failure(self, mock_web3, mock_getenv):
        # Test retrieving wallet balance with failure
        mock_getenv.return_value = 'https://infura_url_here'
        web3_instance = mock_web3.return_value
        web3_instance.eth.get_balance.side_effect = Exception(
            "Something went wrong")

        wallet = Wallet.objects.create(owner=self.user)

        response = self.client.get(f'/api/wallets/{wallet.id}/')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "Failed to fetch wallet balance"})

    def test_retrieve_wallet_not_found(self):
        # Test retrieving a non-existent wallet
        response = self.client.get('/api/wallets/999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Test cases for PoolConditionsViewSet
class PoolConditionsViewSetTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            username='testuser', password='testpassword')
        self.pool_data = {'name': 'Test Pool',
                          'description': 'Test Pool Description'}
        self.pool = StakingPool.objects.create(**self.pool_data)
        self.conditions_data = {
            'staking_pool': self.pool,
            'min_stake': 100.00,
            'annual_interest_rate': 5.00
        }
        self.conditions = PoolConditions.objects.create(**self.conditions_data)

    def test_create_pool_conditions(self):
        # Test creating pool conditions
        view = PoolConditionsViewSet.as_view({'post': 'create'})
        conditions_data = {
            'staking_pool': self.pool.pk,
            'min_stake': 50.00,
            'annual_interest_rate': 7.00
        }
        request = self.factory.post(
            '/api/pool-condition/', data=conditions_data, format='json')
        request.user = self.user
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if new conditions were created
        self.assertEqual(PoolConditions.objects.count(), 2)

    def test_update_pool_conditions(self):
        # Test updating pool conditions
        updated_data = {'min_stake': 75.00}
        view = PoolConditionsViewSet.as_view({'put': 'update'})
        request = self.factory.put(
            f'/api/pool-condition/{self.conditions.pk}/', data=updated_data, format='json')
        request.user = self.user
        self.conditions.refresh_from_db()

    def test_delete_pool_conditions(self):
        # Test deleting pool conditions
        view = PoolConditionsViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(
            f'/api/pool-condition/{self.conditions.pk}/')
        request.user = self.user
        response = view(request, pk=self.conditions.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PoolConditions.objects.count(), 0)

# Test cases for StakingPoolViewSet
class StakingPoolViewSetTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            username='testuser', password='testpassword')
        self.pool_data = {'name': 'Test Pool',
                          'description': 'Test Pool Description'}
        self.pool = StakingPool.objects.create(**self.pool_data)

    def test_create_staking_pool(self):
        # Test creating a staking pool
        view = StakingPoolViewSet.as_view({'post': 'create'})
        request = self.factory.post(
            '/api/staking-pools/', data=self.pool_data, format='json')
        request.user = self.user
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StakingPool.objects.count(), 2)

    def test_update_staking_pool(self):
        # Test updating a staking pool
        updated_data = {'name': 'Updated Pool Name'}
        view = StakingPoolViewSet.as_view({'put': 'update'})
        request = self.factory.put(
            f'/api/staking-pools/{self.pool.pk}/', data=updated_data, format='json')
        request.user = self.user
        self.pool.refresh_from_db()

    def test_delete_staking_pool(self):
        # Test deleting a staking pool
        view = StakingPoolViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/api/staking-pools/{self.pool.pk}/')
        request.user = self.user
        response = view(request, pk=self.pool.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(StakingPool.objects.count(), 0)