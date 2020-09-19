def is_valid(sides):
    # all sides must be greater than 0
    if all(side > 0 for side in sides):
        longest = sides[2]
        short_sum = sides[0] + sides[1]
        return short_sum >= longest
    else:
        return False


def equilateral(sides):
    sides.sort()
    if is_valid(sides):
        return all(side == sides[0] for side in sides)
    return False


def isosceles(sides):
    sides.sort()
    if is_valid(sides):
        # since sides is a sorted list compare the 2nd side with 1st and 3rd
        return sides[1] == sides[0] or sides[1] == sides[2]
    return False


def scalene(sides):
    sides.sort()
    if is_valid(sides):
        return not isosceles(sides)
    return False
