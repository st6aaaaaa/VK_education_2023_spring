import unittest
from lru_cache import LRUCache


class TestLRU(unittest.TestCase):

    def test_lru_1(self):
        cache = LRUCache(2)
        cache.set("k_1", "val_1")
        cache.set("k_2", "val_2")
        self.assertEqual(cache.get("k_3"), None)
        self.assertEqual(cache.get("k_2"), "val_2")
        self.assertEqual(cache.get("k_1"), "val_1")
        cache.set("k_3", "val_3")
        self.assertEqual(cache.get("k_3"), "val_3")
        self.assertEqual(cache.get("k_2"), None)
        self.assertEqual(cache.get("k_1"), "val_1")

    def test_lru_2(self):
        cache = LRUCache()
        cache.set("k_1", "val_1")
        cache.set("k_2", "val_2.1")
        cache.set("k_3", "val_3")
        cache.set("k_4", "val_4")
        self.assertEqual(cache.get("k_3"), "val_3")
        self.assertEqual(cache.get("k_2"), "val_2.1")
        cache.set("k_5", "val_5")
        self.assertEqual(cache.get("k_1"), None)
        self.assertEqual(cache.get("k_3"), "val_3")
        cache.set("k_2", "val_2.2")
        self.assertEqual(cache.get("k_2"), "val_2.2")
        cache.set("k_1", "val_1")
        self.assertEqual(cache.get("k_1"), "val_1")
        self.assertEqual(cache.get("k_4"), None)
