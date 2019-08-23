# -*- coding:utf-8 -*-
# @Time    : 2019/8/23 9:37
# @Author  : Junwu Yu

'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
'''


class Trie:
    # 这种做法完全没体现到树
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.list = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word not in self.set:
            self.set.add(word)
            self.list.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.set

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for s in self.list:
            if s.startswith(prefix):
                return True
        return False


class Trie_:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            # 一层层字典的嵌套
            if s not in node.keys():
                node[s] = {}
            node = node[s]

        # 结束的标志
        node['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                return False

        if 'is_word' in node.keys():
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for s in prefix:
            if s in node.keys():
                node = node[s]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
