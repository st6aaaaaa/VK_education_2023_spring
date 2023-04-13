from collections import deque


class LRUCache:

    def __init__(self, limit=4):
        self.deq = deque(maxlen=limit)
        self.diction = dict()

    def get(self, key):
        list_of_keys = [item[0] for item in self.deq]
        if key in list_of_keys:
            index = list_of_keys.index(key)
            var = self.deq[index]
            self.deq.remove(var)
            self.deq.append(var)
        return self.diction.get(key, None)

    def set(self, key, value) -> None:
        list_of_keys = [item[0] for item in self.deq]
        if key not in list_of_keys:
            if len(self.deq) == self.deq.maxlen:
                del self.diction[self.deq[0][0]]
                self.deq.popleft()
            self.deq.append([key, value])
            self.diction[key] = value
        else:
            index = list_of_keys.index(key)
            self.deq.remove(self.deq[index])
            self.deq.append([key, value])
            self.diction[key] = value
