import random

from SkipNode import SkipNode


class SkipList:
    def __init__(self, max_height):
        self.header = SkipNode(max_height, -int("inf"), None)
        self.max_height = max_height
        self.current_height = 1

    def search(self, search_key):
        """
        Searches for the node with the given key in the Skip List. If the key is found, then the corresponding nodes
        value is returned. Else None is returned. 
        """

        current_node = self.header

        # Start from top level and move down.
        for i in reversed(range(0, self.current_height)):

            # Move forward in the skip list in the current level.
            while current_node.forward[i].key < search_key:
                current_node = current_node.forward[i]
        current_node = current_node.forward[0]
        if current_node is not None and current_node.key == search_key:
            return current_node.value
        
        return None

    def insert(self, insert_key, insert_value):
        """
        Inserts the given element into the Skip List. If no node exists with the given key, 
        then a new node will be created. If a node with the given key already exists, then 
        the node's value will be updated.
        """

        """
        pseudo code
        ============

        update = list of length current_height
        current_node = header

        for i from current_height to 0
            while current_node's ith forward reference's key < insert_key: (and not None)
                current_node = current_node's ith forward reference
            update[i] = current_node
        current_node = current_node's 0th forward reference

        if current_node.key == key:
            current_node.value = insert_value
        
        else:
            new_height = random height
            if new_height > lists current height:
                for i from current_height + 1 to new_height (inclusive):
                    update[i] = header
                current_height = new_height
            new_node = Node(.....)
            for i from 0 to height (exclusive):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
        """

        update = [None] * self.max_height
        current_node = self.header

        for i in reversed(range(self.current_height)):
            while current_node.forward[i] is not None and current_node.forward[i].key < insert_key:
                current_node = current_node.forward[i]
            update[i] = current_node
        

def get_random_height(max_height) -> int:
    """
    Returns a random height in [1...max_height].    
    """

    height = 1

    while random.choice([True, False]) and height < max_height:
        height += 1
    
    return height


