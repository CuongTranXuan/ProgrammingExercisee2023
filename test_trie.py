import unittest
from trie import Trie, TrieNode

class TestTrie(unittest.TestCase):
    def test_insert(self):
        trie = Trie(operator="test")
        trie.insert("0234", cost=1)
        self.assertTrue(trie.search("023482934") == ("test", 1))
        self.assertFalse(trie.search("0123482934") == ("test",1))

    def test_search(self):
        trie = Trie(operator="test")
        trie.insert("0234", cost=1)
        self.assertTrue(trie.search("023482934") == ("test", 1))
        self.assertTrue(trie.search("0234") == ("test", 1))
        self.assertFalse(trie.search("0123482934") == ("test", 1))

if __name__ == '__main__':
    unittest.main()
