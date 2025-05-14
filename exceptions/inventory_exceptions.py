class InventoryException(Exception):
    pass

class InsufficientStockError(InventoryException):
    pass

class DuplicateProductError(InventoryException):
    pass

class InvalidProductDataError(InventoryException):
    pass

class ProductNotFoundError(InventoryException):
    pass