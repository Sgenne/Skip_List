import random

from SkipNode import SkipNode

class SkipList:
    def __init__(self, max_height):
        self.header = SkipNode(max_height, float("-inf"), None)
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

        update = [None] * self.max_height
        current_node = self.header

        for i in reversed(range(self.current_height)):
            while current_node.forward[i] is not None and current_node.forward[i].key < insert_key:
                current_node = current_node.forward[i]
            update[i] = current_node
        current_node = current_node.forward[0]

        # If a node with the given key already exists then update the node's value. 
        if current_node is not None and current_node.key == insert_key:
            current_node.value = insert_value
        
        else:
            new_height = get_random_height(self.max_height)
            
            if new_height > self.current_height:
                for i in range(self.current_height, new_height):
                    update[i] = self.header
                self.current_height = new_height
            
            new_node = SkipNode(new_height, insert_key, insert_value)
            for i in range(0, new_height):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

        

def get_random_height(max_height) -> int:
    """
    Returns a random height in [1...max_height].    
    """

    height = 1

    while random.choice([True, False]) and height < max_height:
        height += 1
    
    return height

def print_skip_list(skip_list:SkipList):
    """
    node_lists = []
    For each node:
        create list of length current_height.
        add key/value to as many elements as the height of the node.
        add list to node_lists
    Create header/NIL lists of length current_height
    add to begining and end of node_list
    for each row starting from current_height:
        for i in len(node_lists):
            if current node list has ith element:
                add to string
        print row


    """
    node_lists = []

    header_list = ["HEAD -> "] * skip_list.current_height
    node_lists.append(header_list)
    
    current_node = skip_list.header.forward[0]

    while current_node is not None:
        node_list = [None] * skip_list.current_height
        for i in range(len(current_node.forward)):
            node_list[i] = f"({current_node.key}, {current_node.value}) -> "
        node_lists.append(node_list)

        current_node = current_node.forward[0]
    
    nil_list = ["NIL"] * skip_list.current_height
    node_lists.append(nil_list)

    for i in reversed(range(skip_list.current_height)):
        row = ""

        for node_list in node_lists:
            if node_list[i] is not None:
                row += node_list[i]
            else:
                row += "    ->    "
        print(row)

    




