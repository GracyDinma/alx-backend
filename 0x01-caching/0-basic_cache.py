#!/usr/bin/env python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache implements a simple caching system without
    limits."""

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item
        value for the key.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        if key or item is None, this method does not do anything.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.
            
        Returns:
            The value in self.cache_data linked to key.
            or None if key is None or does not exist.
        """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
