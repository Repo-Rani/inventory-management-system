from models.product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

    @property
    def size(self):
        return self._size

    @property
    def material(self):
        return self._material

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Type: Clothing, Size: {self._size}, Material: {self._material}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'size': self._size,
            'material': self._material
        })
        return data