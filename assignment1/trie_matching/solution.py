# python3
import sys
from trie_matching import TrieMatching

def solve(text, n, patterns):
	trie = TrieMatching()
	trie.add_patterns(patterns)
	return trie.matches(text)

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
