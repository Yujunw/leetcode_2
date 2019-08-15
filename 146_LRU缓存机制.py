# -*- coding:utf-8 -*-
# @Time    : 2019/8/15 8:54
# @Author  : Junwu Yu

'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
'''
'''
字典本身是无序的，所以我们还需要一个类似于队列的结构来记录访问的先后顺序，这个队列需要支持如下几种操作：

在末尾加入一项
去除最前端一项
将队列中某一项移到末尾

定义使用记录为queue，先进先出，最新的使用记录进队列，则最近未使用的记录出队列，错误，无法将队列中某一项移到末尾，同理list也不行

对于单链表，哈希表的结构类似于 {key: ListNode(value)}，即键所对应的是一个节点地址，节点的值是 value。对于链表，
遇到上面那种情况时可以在常数的时间内找到对应的节点，但是如果想将它移到尾部则需要从头遍历到该节点才能保证链表不断，
对于这种情况需要的时间复杂度也是O(n)，因此使用双向链表

双向链表的头节点和尾节点并不存储数据，头节点之后的一个节点和尾节点之前的一个节点来存储数据使用记录
'''
import queue


class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        # 将node插入到尾节点前
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # key就是原来的key，但是hashmap[key]是一个ListNode
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 如果达到数量限制，删除头节点之后的第一个节点
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            new_node = ListNode(key, value)
            # 将新节点放在尾节点之前
            self.hashmap[key] = new_node
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node


#
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
