from typing import Dict, List, Type, Union
from models.product import Product
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from exceptions.inventory_exceptions import *

class Inventory:
    def __init__(self):
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        if product.product_id in self._products:
            raise DuplicateProductError(f"Product with ID {product.product_id} already exists")
        self._products[product.product_id] = product

    def remove_product(self, product_id: str):
        if product_id not in self._products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        del self._products[product_id]

    def search_by_name(self, name: str) -> List[Product]:
        return [product for product in self._products.values() if name.lower() in product.name.lower()]

    def search_by_type(self, product_type: Type[Product]) -> List[Product]:
        return [product for product in self._products.values() if isinstance(product, product_type)]

    def list_all_products(self) -> List[Product]:
        return list(self._products.values())

    def sell_product(self, product_id: str, quantity: int):
        if product_id not in self._products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product = self._products[product_id]
        try:
            product.sell(quantity)
        except ValueError as e:
            raise InsufficientStockError(str(e))

    def restock_product(self, product_id: str, quantity: int):
        if product_id not in self._products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product = self._products[product_id]
        try:
            product.restock(quantity)
        except ValueError as e:
            raise InvalidProductDataError(str(e))

    def total_inventory_value(self) -> float:
        return sum(product.get_total_value() for product in self._products.values())

    def remove_expired_products(self) -> List[str]:
        expired_ids = []
        for product_id, product in list(self._products.items()):
            if isinstance(product, Grocery) and product.is_expired():
                expired_ids.append(product_id)
                del self._products[product_id]
        return expired_ids

    def to_dict(self) -> List[Dict]:
        return [product.to_dict() for product in self._products.values()]