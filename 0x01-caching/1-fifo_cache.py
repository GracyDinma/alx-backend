#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self):
but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache implements a FIFO caching system."""

    def __init__(self):
        """Initialize the FIFO cache and call the parent init.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item
        value for the key key.

        Args:
            key: The key under which the item is stored.
            items: The item to be stored in the cache.

        if key or item is NOne, this method does not do anything.
        if adding this item exceeds MAX_ITEMS,
        the first item added is discarded.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns: The value in self.cache_data linked to key.
        or None if key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
