#!/usr/bin/python3
"""
Module documentation for 0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """

    collected_keys = {0}
    key = boxes[0]

    def search_box(box):
        for key in boxes[box]:
            if key > len(boxes) - 1:
                # invalid key
                continue
            if key not in collected_keys:
                collected_keys.add(key)
                search_box(key)

    search_box(0)
    return len(collected_keys) == len(boxes)
