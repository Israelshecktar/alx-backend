#!/usr/bin/env python3
"""Module for BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching.
    A simple caching system that stores entries in a dictionary without
    """

    def put(self, key, item):
        """Add an item in the cache with a given key.
        Args:
            key (str): Key where the item needs to be stored.
            item (str): Item that needs to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key.
        Args:
            key (str): Key which needs to be accessed.
        Returns:
            str: Value associated with key if it exists, None otherwise.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
