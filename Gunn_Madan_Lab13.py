import math
import os
import random
import re
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, name):
        current = self.root
        for char in name:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.count += 1
            
    def find(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.count

def contacts(queries):
    trie = Trie()
    results = []
    
    for operation , value in queries:
        if operation == 'add':
            trie.add(value)
        elif operation == 'find':
                results.append(trie.find(value))
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
