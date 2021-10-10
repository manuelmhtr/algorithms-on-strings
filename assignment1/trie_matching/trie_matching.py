# python3
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.join(parentdir, 'trie'))

from trie import Trie

class TrieMatching(Trie):
	EOP = '$'

	def add_patterns(self, patterns):
		for pattern in patterns:
			self.add_pattern(pattern + self.EOP, 0)

	def matches(self, text):
		results = []
		for i in range(len(text)):
			if self.check_match(text[i:], 0):
				results.append(i)
		return results

	def check_match(self, text, node):
		if self.EOP in self.tree.get(node, {}):
			return True
		if not text:
			return False
		to_node = self.tree.get(node, {}).get(text[0])
		if to_node:
			return self.check_match(text[1:], to_node)
		return False
