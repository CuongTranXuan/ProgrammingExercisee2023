from typing import List
from trie import Trie
import json


phone_prefixes = {
  "operatorA": [
    {
      "prefix": "0123",
      "cost": 1.1
    },
    {
      "prefix": "012345",
      "cost": 2.2
    }
  ],
  "operatorB": [
    {
      "prefix": "01",
      "cost": 3.3
    },
    {
      "prefix": "012345",
      "cost": 4.4
    }
  ],
  "operatorC": [
    {
      "prefix": "6789",
      "cost": 5.5
    }
  ]
}

def create_forest(prefixes: List) -> List[Trie]:
    """
    Creates a forest of Trie objects based on the given phone prefixes.

    Parameters:
        phone_prefixes (List): A list of dictionaries representing phone prefixes.

    Returns:
        List[Trie]: A list of Trie objects representing the forest of phone number prefixes.
    """
    forest = []
    for operator in prefixes:
        trie = Trie(operator)
        for prefix in prefixes[operator]:
            trie.insert(prefix["prefix"], prefix["cost"])
        forest.append(trie)
    return forest

def find_all_prefixes(forest: List[Trie], number: str) -> str:
    """
    Finds every prefixes available and cost if using the phone number with each operator

    Args:
        forest: A trie forest.
        number: The input phone number.
    Returns:
        list prefix and cost for each operator
    """
    # Initialize the longest_prefix variable to an empty string
    result = []
    for tree in forest:
        prefix, cost = tree.search(number)
        result.append((prefix, cost))

    # Return the longest common prefix
    return result

if __name__ == '__main__':
    test_forest = create_forest(phone_prefixes)
    print(find_all_prefixes(test_forest, '012399999'))
