class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, limit=4):
        self.diction = {}
        self.cur_size = 0
        self.max_size = limit
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def removenode(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def movetoend(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.diction.keys():
            return None
        node = self.diction[key]
        self.removenode(node)
        self.movetoend(node)
        return node.val

    def set(self, key, new_val):
        if key in self.diction.keys():
            node = self.diction[key]
            node.val = new_val
            self.removenode(node)
            self.movetoend(node)
        else:
            if self.cur_size >= self.max_size:
                lru_node = self.head.next
                del self.diction[lru_node.key]
                self.removenode(lru_node)
                self.cur_size -= 1
            new_node = Node(key, new_val)
            self.diction[key] = new_node
            self.movetoend(new_node)
            self.cur_size += 1
             
