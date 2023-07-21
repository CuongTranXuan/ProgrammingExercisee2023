import unittest
from trie import Trie, TrieNode

class TestTrie(unittest.TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("banana"))

    def test_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.search("app"))
        self.assertFalse(trie.search("banana"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("app"))
        self.assertFalse(trie.starts_with("ban"))

if __name__ == '__main__':
    unittest.main()
