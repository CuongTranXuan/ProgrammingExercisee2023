from typing import List


class TrieNode:
    """
    Attributes:
        children (Dict[str, TrieNode]): The children nodes of the current node.
        value (float): the leaf node contain the value of that string, otherwise -1.

    Methods:
        __init__() -> None: Initializes a new instance of the TrieNode class.
    """
    def __init__(self, value):
        self.children = {}
        self.value = value


class Trie:
    """
    A class representing a trie data structure.

    Attributes:
        root (TrieNode): The root node of the trie.
        operator (str): operator that every prefix belongs to.

    Methods:
        insert(prefix: str, cost: float) -> None: Inserts a phone number into the trie with its cost
        search(number: str) -> prefix, cost: search the longest prefix that matches the phone number from the trie.
    """
    def __init__(self, operator):
        self.root = TrieNode(-1)
        self.operator = operator # this trie belongs to which operator

    def insert(self, prefix, cost):
        """
        Inserts a phone number into the trie.

        Parameters:
            phone_number (str): The phone number to be inserted into the trie.

        Returns:
            None
        """
        node = self.root
        for digit in prefix:
            if digit not in node.children:
                node.children[digit] = TrieNode(-1)
            node = node.children[digit]
        node.value = cost
    
    def search(self, number):
        """
        Searches for a longest common prefix between the phone number and the trie.
        """
        node = self.root
        prefix = ""
        value = -1
        for digit in number:
            if digit in node.children:
                prefix += digit
                node = node.children[digit]
                if node.value != -1:
                    value = node.value
            else:
                break
        return self.operator, value