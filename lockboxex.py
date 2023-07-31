from typing import List


def canUnlockAll(boxes: List[list]) -> bool:
    unlocked_boxes = {}
    try:
        empty_index = boxes.index([])
        boxes[empty_index] = [0]
    except Exception:
        pass
    some = [x for x in range(len(boxes))]
    # print(some)
    unlocked_boxes[0] = 'unlocked'
    for i in range(len(boxes) - 1):
        # if i in opened_boxes:
        for k in range(len(boxes[i])):
            if boxes[i][k] in some:
                unlocked_boxes[boxes[i][k]] = 'unlocked'

    opened = unlocked_boxes.values()
    print(unlocked_boxes)
    # print(opened)
    if len(opened) != len(boxes):
        return False
    return True


boxes: List[list] = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
