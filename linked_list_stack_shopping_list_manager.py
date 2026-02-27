# Declare node class
class Node:
    # Define __init__ function
    # Parameter: data for the node
    def __init__(self, data):
        # Initialize data to specified value
        # Initialize next node to None (empty)
        self.data = data
        self.next = None
        
# Declare Linked List class
class LinkedListStackShoppingListManagerClass:
    # Define __init__ function
    def __init__(self):
        # Initialize head node to None (empty)
        self.head = None

    # Define insert_item function to insert an item on the top of the stack
    # Parameter: item to insert into the stack
    def insert_item(self, item):
        # If stack is empty (head is None), set item to insert as head node
        # Else, Create new node with item to insert as data
        # Set current head node as new node's next node
        # Set new node as head node
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    # Define is_list_empty function to check if stack is empty
    def is_list_empty(self):
        # Check if head node is None. Then return True
        # Else return False 
        return self.head is None

    # Define print_item_recursive_from_top method to print items in stack recursively from top
    # Parameter: currentNode to print
    def print_item_recursive_from_top(self, currentNode):
        # Base case: if currentNode is None, return from recursion
        if currentNode is None:
            return
        
        # Else, Recursive case
        # Recursive call with the next nodePrint the currentNode's data
        print(currentNode.data, end = " ")
        self.print_item_recursive_from_top(currentNode.next)

    # Define print_items_from_top function to call print_item_recursive_from_top function
    def print_items_from_top(self):
        # Call print_item_recursive_from_top function with head node
        print("[", end = " ")
        self.print_item_recursive_from_top(self.head)
        print("]")

    # Define print_item_recursive_from_bottom method to print the items in the
    # stack recursively from the bottom
    # Parameter: currentNode to print
    def print_item_recursive_from_bottom(self, currentNode):
        # Base case: if the currentNode is None, return from the recursion
        if currentNode is None:
            return
        
        # Else, Recursive case
        # Print currentNode's data. Recursive call with the next node
        self.print_item_recursive_from_bottom(currentNode.next)
        print(currentNode.data, end = " ")

    # Define print_items_from_bottom function to call print_item_recursive_from_bottom function
    def print_items_from_bottom(self):
        # Call print_item_recursive_from_bottom function with head node
        print("[", end = " ")
        self.print_item_recursive_from_bottom(self.head)
        print("]")

    # Define getLastItem function to return last item inserted into stack (peek operation)
    def getLastItem(self):
        # Check if stack is empty. Then return None
        # Else, Return the head node's data
        if self.is_list_empty():
            return None
        
        return self.head.data

    # Define removeLastItem function to remove last item inserted into stack (pop operation)
    def removeLastItem(self):
        # Check if stack is empty. Then Return None
        if self.is_list_empty():
            return None
        
        # Else, Define node to "pop" as head node. Set head node to current head node's next node
        # Set popped node's next pointer to None. Return popped node's data
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None

        return popped_node.data