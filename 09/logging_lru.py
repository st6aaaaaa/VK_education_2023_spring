import sys
import logging.config
import logging


class CustomFilter(logging.Filter):
    def filter(self, record):
        return len(record.msg.split()) % 2 == 1


log_config = {
            "version": 1,
            "handlers": {
                    "file": {
                             "filename": "cache.log",
                             "level": "DEBUG",
                             "class": "logging.FileHandler",
                             "formatter": "out"},

                    "console": {
                            "class": "logging.StreamHandler",
                            "level": "DEBUG",
                            "formatter": "output_console"},

                    "onlyfilter": {
                            "filename": "cache.log",
                            "level": "DEBUG",
                            "class": "logging.FileHandler",
                            "formatter": "out",
                            "filters": ["filter"]},

                    "consolewithfilter": {
                            "level": "DEBUG",
                            "class": "logging.StreamHandler",
                            "formatter": "output_console",
                            "filters": ["filter"]},
                },

            "formatters": {
                        "out": {
                                "format": "%(levelname)s %(message)s"
                            },
                        "output_console": {
                                "format": "%(levelname)s Good evening - "
                                          "console  %(message)s"
                            }
                        },

            "loggers": {
                        "logfile": {
                                "handlers": ["file"],
                                "level": "DEBUG"
                            },
                        "logconsole": {
                                "handlers": ["console", "file"],
                                "level": "DEBUG"
                            },
                        "logfilter": {
                                "handlers": ["onlyfilter"],
                                "level": "DEBUG"
                            },
                        "logconsoleandfilter": {
                                "handlers": ["consolewithfilter",
                                             "onlyfilter"],
                                "level": "DEBUG"
                            }
                    },

            "filters": {
                    "filter": {
                            "()": CustomFilter
                        }
                }
        }

logging.config.dictConfig(log_config)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, console, filtset, limit=4):
        if console and filtset:
            self.logger = logging.getLogger("logconsoleandfilter")
        elif console and not filtset:
            self.logger = logging.getLogger("logconsole")
        elif not console and filtset:
            self.logger = logging.getLogger("logfilter")
        else:
            self.logger = logging.getLogger("logfile")

        if limit < 0:
            self.logger.error("ошибка! емкость должна быть неотрицательной")
            raise ValueError("емкость неположительна")

        self.logger.info("инициализация")

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
            self.logger.info("метод get, ключ отсутствует")
            return None
        self.logger.info("метод get, ключ присутствует")
        node = self.diction[key]
        self.removenode(node)
        self.movetoend(node)
        return node.val

    def set(self, key, new_val):
        if key in self.diction.keys():
            self.logger.info("метод set, установка существующего ключа")
            node = self.diction[key]
            node.val = new_val
            self.removenode(node)
            self.movetoend(node)

        else:
            flag = True
            if self.cur_size >= self.max_size:
                self.logger.info("метод set, "
                                 "установка нового ключа "
                                 "при достигнутой емкости")
                lru_node = self.head.next
                del self.diction[lru_node.key]
                self.removenode(lru_node)
                self.cur_size -= 1
                flag = False
            if flag:
                self.logger.info(
                    "метод set, установка нового ключа "
                    "при НЕдостигнутой емкости")
            new_node = Node(key, new_val)
            self.diction[key] = new_node
            self.movetoend(new_node)
            self.cur_size += 1


if __name__ == '__main__':
    tmp = sys.argv
    consol = '-s' in tmp
    filt = '-f' in tmp
    d = LRUCache(consol, filt, 3)
    d.set('key_1', 'val_1')
    d.set('key_2', 'val_2')
    d.set('key_1', 'val_1')
    d.set('key_3', 'val_3')
    d.set('key_4', 'val_4')
    d.get('key_2')
    d.get('key_1')
     
