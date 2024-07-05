#!/usr/bin/python3
"""
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    returns true or false

    Args:
         boxes: list of lists
    Return:
         true or false
    """
    def box(index):
        if index in unlocked_boxes:
            return
        unlocked_boxes.add(index)
        for key in boxes[index]:
            if key < len(boxes):
                box(key)

    unlocked_boxes = set()
    box(0)

    return len(unlocked_boxes) == len(boxes)
