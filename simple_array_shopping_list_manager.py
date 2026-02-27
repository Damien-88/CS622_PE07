class SimpleArrayShoppingListManagerClass:
    # Define __init__ function
    def __init__(self):
        # Initialize empty shopping_list array
        self.shopping_list = []

    # Define insert_item function to insert items into list
    # Parameter: item to insert into beginning of list
    def insert_item(self, item):
        self.shopping_list.insert(0, item)

    # Define print_items function to print items in list
    def print_items(self):
        # Print all items in list
        print("[", end = " ")
        print(", ".join(self.shopping_list), end = " ")
        print("]")