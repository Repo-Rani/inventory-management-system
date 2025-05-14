from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Sale quantity must be positive")
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock available")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        return f"ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f}, Stock: {self._quantity_in_stock}"

    def to_dict(self):
        """Convert product to dictionary for JSON serialization"""
        return {
            'type': self.__class__.__name__,
            'product_id': self._product_id,
            'name': self._name,
            'price': self._price,
            'quantity_in_stock': self._quantity_in_stock
        }