#!/usr/bin/env python3
"""
Module providing pagination helpers.

This module provides functions to assist with implementing pagination
"""


def index_range(page, page_size):
    """
    Calculate the start and end index for items on a given page.

    :param page: int - Current page number (1-indexed)
    :param page_size: int - Number of items per page
    :return: tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
