class PriceHashTable:
    def __init__(self, size=128):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def custom_hash(self, item_name):
        """Custom hash function using polynomial rolling hash"""
        hash_value = 0
        for i, char in enumerate(str(item_name)):
            hash_value += ord(char) * (31 ** i)
        return hash_value % self.size
    
    def insert(self, item_name, price):
        """Insert an item and its price into the hash table"""
        index = self.custom_hash(item_name)
        for i, (existing_item, _) in enumerate(self.table[index]):
            if existing_item == item_name:
                self.table[index][i] = (item_name, price)
                return
        self.table[index].append((item_name, price))
    
    def get_price(self, item_name):
        """Retrieve price for a given item"""
        index = self.custom_hash(item_name)
        for existing_item, price in self.table[index]:
            if existing_item == item_name:
                return price
        return None
    
    def display_all(self):
        """Display all items and their prices"""
        all_items = []
        for bucket in self.table:
            all_items.extend(bucket)
        return sorted(all_items, key=lambda x: x[0])

import random

def generate_sample_items(num_items=100):
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home']
    items = []
    
    for i in range(num_items):
        category = random.choice(categories)
        item_name = f"{category}_{i+1}"
        if category == 'Electronics':
            price = round(random.uniform(100, 2000), 2)
        elif category == 'Clothing':
            price = round(random.uniform(20, 200), 2)
        elif category == 'Food':
            price = round(random.uniform(2, 50), 2)
        elif category == 'Books':
            price = round(random.uniform(10, 100), 2)
        else:
            price = round(random.uniform(30, 500), 2)
        items.append((item_name, price))
    return items

price_table = PriceHashTable()

sample_items = generate_sample_items(100)
for item_name, price in sample_items:
    price_table.insert(item_name, price)

def demonstrate_usage():
    print("First 10 items in the price list:")
    all_items = price_table.display_all()
    for item, price in all_items[:10]:
        print(f"{item}: ${price:.2f}")

    print("\nLooking up some specific items:")
    test_items = [all_items[0][0], all_items[50][0], all_items[-1][0]]
    for item in test_items:
        price = price_table.get_price(item)
        print(f"{item}: ${price:.2f}")

    print("\nPrice List Statistics:")
    prices = [price for _, price in all_items]
    print(f"Number of items: {len(all_items)}")
    print(f"Average price: ${sum(prices)/len(prices):.2f}")
    print(f"Highest price: ${max(prices):.2f}")
    print(f"Lowest price: ${min(prices):.2f}")

if __name__ == "__main__":
    demonstrate_usage()