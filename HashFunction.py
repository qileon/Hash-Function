import json
import os

def hash_function(item_name):
    if len(item_name) == 1:
        return ord(item_name) % 991 + 10
    
    first_char_ascii = ord(item_name[0])
    second_char_ascii = ord(item_name[1]) if len(item_name) > 1 else 0
    last_char_ascii = ord(item_name[-1])
    second_last_char_ascii = ord(item_name[-2]) if len(item_name) > 1 else 0
    
    ascii_sum = first_char_ascii + second_char_ascii + last_char_ascii + second_last_char_ascii
    
    price = ascii_sum % 991 + 10
    return price

def add_to_price_list(price_list, item_name):
    price = hash_function(item_name)
    price_list[item_name] = price
    save_price_list(price_list)

def remove_from_price_list(price_list, item_name):
    if item_name in price_list:
        del price_list[item_name]
        save_price_list(price_list)
        print(f"'{item_name}' has been removed from the price list.")
    else:
        print(f"'{item_name}' not found in the price list.")

def display_price_list(price_list):
    print("\nCurrent Price List:")
    for item in sorted(price_list.keys()):
        print(f"{item}: {price_list[item]}")
    print()

def load_price_list(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_price_list(price_list, filename='price_list.json'):
    with open(filename, 'w') as file:
        json.dump(price_list, file)

def initialize_price_list():
    grocery_items = [
        "Eggs", "Apple", "Banana", "Milk", "Cheese", "Yogurt", "Bread", "Flour", "Sugar", "Salt",
        "Olive Oil", "Pasta", "Kidney Beans", "Lentils", "Bulgur", "Rice", "Coffee", "Tea", "Honey", "Jam",
        "Sauce", "Ketchup", "Mayonnaise", "Pepper", "Tomato", "Cucumber", "Carrot", "Potato", "Onion",
        "Garlic", "Broccoli", "Cauliflower", "Spinach", "Lettuce", "Arugula", "Celery", "Cabbage", "Corn", "Hazelnut",
        "Walnut", "Dried Apricot", "Dried Grape", "Pine Nut", "Dried Pomegranate", "Ice Cream", "Biscuit", "Chocolate", "Pistachio",
        "Fruit Juice", "Soda", "Sparkling Water", "Buttermilk", "Lemonade", "Pasta Sauce", "Chicken Sauce", "Chicken Breast", "Red Meat",
        "Meatballs", "Fish", "Sardines", "Tuna", "Canned Food", "Liquid Soap", "Dish Detergent", "Laundry Detergent", "Personal Care",
        "Toothpaste", "Shampoo", "Soap", "Body Lotion", "Face Cream", "Perfume", "Towel", "Toilet Paper", "Tissue", "Diaper",
        "Baby Food", "Cat Food", "Dog Food", "Animal Feed", "Drink", "Olives", "Pepper Paste", "Tomato Paste", "Breakfast Cereal", "Granola",
        "Muesli", "Iced Tea", "Coconut", "Spices", "Chickpeas", "Soy Sauce", "Cake", "Tortilla", "Pizza", "Sushi",
        "Sausage", "Cornflakes", "Snack", "Chocolate Chips", "Cake Flour", "Milk Powder", "Cookie Mix", "Cake Ingredients"
    ]
    
    price_list = load_price_list('price_list.json')
    
    for item in grocery_items:
        if item not in price_list:
            add_to_price_list(price_list, item)
    
    return price_list

def main():
    price_list = initialize_price_list()
    
    while True:
        action = input("Type 'add' to add an item, 'get' to get an item's price, 'remove' to remove an item, 'list' to display the price list, or 'exit' to quit: ").lower()
        
        if action == 'exit':
            break
        
        if action == 'add':
            item_name = input("Enter the name of an item: ")
            if item_name not in price_list:
                add_to_price_list(price_list, item_name)
                print(f"The price for '{item_name}' has been added.")
            else:
                print(f"'{item_name}' is already in the price list.")

        elif action == 'get':
            user_input = input("Type the item name to get its price: ")
            if user_input in price_list:
                print(f"The price for '{user_input}' is: {price_list[user_input]}")
            else:
                print(f"'{user_input}' not found in the price list.")
        
        elif action == 'remove':
            item_name = input("Enter the name of the item to remove: ")
            remove_from_price_list(price_list, item_name)
        
        elif action == 'list':
            display_price_list(price_list)

if __name__ == "__main__":
    main()
