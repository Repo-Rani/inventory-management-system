from datetime import datetime
from models.product import Product

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    @property
    def expiry_date(self):
        return self._expiry_date

    def is_expired(self):
        return datetime.now().date() > self._expiry_date

    def __str__(self):
        base_info = super().__str__()
        status = "EXPIRED" if self.is_expired() else "VALID"
        return f"{base_info}, Type: Grocery, Expiry: {self._expiry_date}, Status: {status}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'expiry_date': self._expiry_date.strftime("%Y-%m-%d")
        })
        return data