from typing import Any, Dict
from datetime import datetime, timedelta
from rest_framework import status
from utils.base_test_api import BaseAPITestCase


class BaseProductTestCase(BaseAPITestCase):
    
    def create_product(
        self,
        name: str = 'New Product',
        description: str = 'New Description',
        stock_quantity: int = 10,
        days_to_expire: int = 10
    ) -> Dict[str, Any]:
        """
        Create a new product.

        Args:
        - name (str): The name of the product.
        - description (str): The description of the product.
        - stock_quantity (int): The quantity of the product in stock.
        - days_to_expire (int): The number of days until the product expires.

        Returns:
        - dict: The created product data.
        """
        data = {
            'name': name,
            'description': description,
            'stock_quantity': stock_quantity,
            'expiration_date': (datetime.now() + timedelta(days=days_to_expire)).strftime('%Y-%m-%d')
        }
        response = self.client.post('/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data


class ProductViewSetTestCase(BaseProductTestCase):
    """
    Test case for the ProductViewSet.
    """

    def test_product_list(self) -> None:
        """
        Test the ProductViewSet list method (GET request).
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_update(self) -> None:
        """
        Test the ProductViewSet update method (PUT request).
        """
        product_data = self.create_product()
        product_id = product_data["id"]
        data = {
            'name': 'Updated Product Name',
            'description': product_data["description"],
            'expiration_date': product_data["expiration_date"],
            'stock_quantity': product_data["stock_quantity"]
        }
        response = self.client.put(f"/products/{product_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_delete(self) -> None:
        """
        Test the ProductViewSet delete method (DELETE request).
        """
        product_data = self.create_product()
        product_id = product_data["id"]
        response = self.client.delete(f'/products/{product_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_product_retrieve(self) -> None:
        """
        Test the ProductViewSet retrieve method (GET request).
        """
        product_data = self.create_product()
        product_id = product_data["id"]
        response = self.client.get(f'/products/{product_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_partial_update(self) -> None:
        """
        Test the ProductViewSet partial_update method (PATCH request).
        """
        product_data = self.create_product()
        product_id = product_data["id"]
        data = {
            'stock_quantity': 30
        }
        response = self.client.patch(f'/products/{product_id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AlertViewSetTestCase(BaseProductTestCase):
    """
    Test case for the AlertViewSet.
    """

    def test_alert_list(self) -> None:
        """
        Test the AlertViewSet list method (GET request).
        """
        response = self.client.get('/alerts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_alert_retrieve(self) -> None:
        """
        Test the AlertViewSet retrieve method (GET request).
        """
        self.create_product()
        alert_id = 1
        response = self.client.get(f'/alerts/{alert_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
