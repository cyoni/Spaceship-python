import math


def distance(p1, p2):
    p1_x = p1.getx()
    p1_y = p1.gety()
    p2_x = p2.getx()
    p2_y = p2.gety()
    return math.sqrt(pow((p1_x - p2_x), 2) + pow((p1_y - p2_y), 2))
