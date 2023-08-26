#!/usr/bin/python3
"""
Module documentation for 0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """

    collected_keys = {0}
    locked_boxes = set(range(1, len(boxes)))
    boxes[0]

    def search_box(box):
        new_keys = (set(boxes[box])
                    .intersection(locked_boxes)
                    .difference(collected_keys))
        for key in new_keys:
            collected_keys.add(key)
        for key in new_keys:
            if key > len(boxes) - 1:
                # invalid key
                continue
            locked_boxes.remove(key)
            if (set(boxes[key])
                    .intersection(locked_boxes)
                    .difference(collected_keys)):
                search_box(key)

    search_box(0)
    return len(locked_boxes) == 0
