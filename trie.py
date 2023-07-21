class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self, value):
        self.root = TrieNode()
        self.value = value

    def insert(self, phone_number):
        node = self.root
        for digit in phone_number:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.is_end_of_number = True

phone_numbers = [{"number":"1234567890","value":10},{"number":"9876543210","value":9},{"number":"5555555555","value":2}, {"number":"1239999999","value":1}]

forest = []
for phone_number in phone_numbers:
    trie = Trie(phone_number["value"])
    trie.insert(phone_number["number"])
    forest.append(trie)

def find_longest_common_prefix(forest, phone_number):
    longest_prefix = ""
    for trie in forest:
        node = trie.root
        prefix = ""
        for digit in phone_number:
            if digit in node.children:
                prefix += digit
                node = node.children[digit]
            else:
                break
        if len(prefix) > len(longest_prefix):
            longest_prefix = prefix
    return longest_prefix

print(find_longest_common_prefix(forest, "123939393939"))

#create unit test for above code snippet
