import unittest
from phone_problem_valuechecker import *
class TestConstructTrieForest(unittest.TestCase):
    def test_single_string(self):
        string_list = ["apple"]
        forest = construct_trie_forest(string_list)
        self.assertEqual(len(forest), 1)
        self.assertEqual(forest[0].children['a'].children['p'].children['p'].children['l'].children['e'].is_word_end, True)

    def test_multiple_strings(self):
        string_list = ["apple", "banana", "cherry"]
        forest = construct_trie_forest(string_list)
        self.assertEqual(len(forest), 3)
        self.assertEqual(forest[0].children['a'].children['p'].children['p'].children['l'].children['e'].is_word_end, True)
        self.assertEqual(forest[1].children['b'].children['a'].children['n'].children['a'].children['n'].children['a'].is_word_end, True)
        self.assertEqual(forest[2].children['c'].children['h'].children['e'].children['r'].children['r'].children['y'].is_word_end, True)

if __name__ == '__main__':
    unittest.main()