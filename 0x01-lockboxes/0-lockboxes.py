#!/usr/bin/python3
"""
Lockboxes problem solution
"""


def canUnlockAll(boxes):
    """
    Checks if a series of locked boxes can be opened
    based on keys that can be attained.
    Solves the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for box in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = box in boxes[idx] and box != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
