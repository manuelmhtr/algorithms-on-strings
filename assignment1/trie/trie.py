#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

class Trie:
    def __init__(self):
        self.tree = {}
        self.nodes_count = 0

    def add_patterns(self, patterns):
        for pattern in patterns:
            self.add_pattern(pattern, 0)

    def add_pattern(self, pattern, from_node):
        if not pattern:
            return
        char = pattern[0]
        to_node = self.tree.get(from_node, {}).get(char)
        if not to_node:
            self.nodes_count += 1
            to_node = self.nodes_count
            self.add_edge(from_node, to_node, char)
        self.add_pattern(pattern[1:], to_node)

    def add_edge(self, from_node, to_node, label):
        self.tree[from_node] = self.tree.get(from_node, {})
        self.tree[from_node][label] = to_node
