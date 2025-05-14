import json
from typing import Dict, List
from models.product import Product
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from exceptions.inventory_exceptions import InvalidProductDataError

def save_to_file(inventory, filename: str):
    """Save inventory to JSON file"""
    with open(filename, 'w') as f:
        json.dump(inventory.to_dict(), f, indent=4)

def load_from_file(filename: str):
    """Load inventory from JSON file"""
    from services.inventory import Inventory
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise InvalidProductDataError(f"Error loading file: {str(e)}")

    inventory = Inventory()
    product_classes = {
        'Electronics': Electronics,
        'Grocery': Grocery,
        'Clothing': Clothing
    }

    for item in data:
        try:
            product_type = item.pop('type')
            if product_type not in product_classes:
                raise InvalidProductDataError(f"Unknown product type: {product_type}")

            if product_type == 'Grocery' and 'expiry_date' in item:
                item['expiry_date'] = item['expiry_date'] 

            product = product_classes[product_type](**item)
            inventory.add_product(product)
        except Exception as e:
            raise InvalidProductDataError(f"Error creating product: {str(e)}")

    return inventory