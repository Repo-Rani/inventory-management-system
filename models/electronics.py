from models.product import Product

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._warranty_years = warranty_years
        self._brand = brand

    @property
    def warranty_years(self):
        return self._warranty_years

    @property
    def brand(self):
        return self._brand

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Type: Electronics, Brand: {self._brand}, Warranty: {self._warranty_years} years"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'warranty_years': self._warranty_years,
            'brand': self._brand
        })
        return data