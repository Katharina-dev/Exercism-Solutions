def is_triangle(sides):
    sides.sort()
    return sides[0] > 0 and sides[0] + sides[1] > sides[2]


def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
