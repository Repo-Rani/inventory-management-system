from services.inventory import Inventory
from utils.json_handler import save_to_file, load_from_file
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from exceptions.inventory_exceptions import *
import sys

def display_menu():
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Search Products")
    print("4. List All Products")
    print("5. Restock Product")
    print("6. Remove Expired Groceries")
    print("7. Save Inventory")
    print("8. Load Inventory")
    print("9. Exit")

def get_product_details():
    print("\nProduct Types:")
    print("1. Electronics")
    print("2. Grocery")
    print("3. Clothing")
    
    p_type = input("Select product type (1-3): ")
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter initial stock quantity: "))
    
    if p_type == "1":
        brand = input("Enter brand: ")
        warranty = int(input("Enter warranty years: "))
        return Electronics(product_id, name, price, quantity, warranty, brand)
    elif p_type == "2":
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        return Grocery(product_id, name, price, quantity, expiry)
    elif p_type == "3":
        size = input("Enter size: ")
        material = input("Enter material: ")
        return Clothing(product_id, name, price, quantity, size, material)
    else:
        print("Invalid product type")
        return None

def main():
    inventory = Inventory()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")
        
        try:
            if choice == "1":
                product = get_product_details()
                if product:
                    inventory.add_product(product)
                    print("Product added successfully!")
            
            elif choice == "2":
                product_id = input("Enter product ID to sell: ")
                quantity = int(input("Enter quantity to sell: "))
                inventory.sell_product(product_id, quantity)
                print("Sale completed successfully!")
            
            elif choice == "3":
                print("\nSearch Options:")
                print("1. By Name")
                print("2. By Type")
                search_choice = input("Select search type (1-2): ")
                
                if search_choice == "1":
                    name = input("Enter product name to search: ")
                    results = inventory.search_by_name(name)
                elif search_choice == "2":
                    print("\nProduct Types:")
                    print("1. Electronics")
                    print("2. Grocery")
                    print("3. Clothing")
                    type_choice = input("Select type to search (1-3): ")
                    
                    if type_choice == "1":
                        results = inventory.search_by_type(Electronics)
                    elif type_choice == "2":
                        results = inventory.search_by_type(Grocery)
                    elif type_choice == "3":
                        results = inventory.search_by_type(Clothing)
                    else:
                        print("Invalid choice")
                        continue
                else:
                    print("Invalid choice")
                    continue
                
                if not results:
                    print("No products found")
                else:
                    print("\nSearch Results:")
                    for product in results:
                        print(product)
            
            elif choice == "4":
                products = inventory.list_all_products()
                if not products:
                    print("Inventory is empty")
                else:
                    print("\nAll Products:")
                    for product in products:
                        print(product)
                    print(f"\nTotal Inventory Value: ${inventory.total_inventory_value():.2f}")
            
            elif choice == "5":
                product_id = input("Enter product ID to restock: ")
                quantity = int(input("Enter quantity to add: "))
                inventory.restock_product(product_id, quantity)
                print("Restock completed successfully!")
            
            elif choice == "6":
                expired = inventory.remove_expired_products()
                if expired:
                    print(f"Removed {len(expired)} expired products: {', '.join(expired)}")
                else:
                    print("No expired products found")
            
            elif choice == "7":
                filename = input("Enter filename to save (e.g., inventory.json): ")
                save_to_file(inventory, filename)
                print("Inventory saved successfully!")
            
            elif choice == "8":
                filename = input("Enter filename to load (e.g., inventory.json): ")
                inventory = load_from_file(filename)
                print("Inventory loaded successfully!")
            
            elif choice == "9":
                print("Exiting the system. Goodbye!")
                sys.exit()
            
            else:
                print("Invalid choice. Please try again.")
        
        except InventoryException as e:
            print(f"Error: {str(e)}")
        except ValueError:
            print("Error: Invalid input format")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()