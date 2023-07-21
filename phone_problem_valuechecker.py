# define a trie structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False


# Example usage:
string_list = ["apple", "banana", "orange"]
trie_forest = construct_trie_forest(string_list)

# define a trie tree contain string of telephone numbers
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# create a trie forest for a list of input telephone prefix numbers
def construct_trie_forest(string_list):
    forest = []
    for string in string_list:
        root = TrieNode()
        node = root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_end = True
        forest.append(root)
    return forest
