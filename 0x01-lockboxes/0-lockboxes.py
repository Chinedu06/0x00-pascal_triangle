#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.
    Args:
        boxes (list of lists): Each list contains keys for other boxes.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is always unlocked
    keys = boxes[0]  # Start with the keys in the first box

    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
