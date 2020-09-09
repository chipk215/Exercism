"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):

    def yacht_func(dice_list):
        if all(item == dice_list[0] for item in dice_list):
            return 50
        else:
            return 0

    def ones_func(dice_list):
        return dice_list.count(1)

    def twos_func(dice_list):
        return 2 * dice_list.count(2)

    def threes_func(dice_list):
        return 3 * dice_list.count(3)

    def fours_func(dice_list):
        return 4 * dice_list.count(4)

    def fives_func(dice_list):
        return 5 * dice_list.count(5)

    def sixes_func(dice_list):
        return 6 * dice_list.count(6)

    def full_house_func(dice_list):
        dice_list.sort()
        if dice_list.count(dice_list[0]) == 2:
            if dice_list.count(dice_list[2]) == 3:
                return sum(dice_list)
            else:
                return 0
        elif dice_list.count(dice_list[0]) == 3:
            if dice_list.count(dice_list[3]) == 2:
                return sum(dice_list)
            else:
                return 0
        else:
            return 0

    def four_kind_func(dice_list):
        dice_list.sort()
        if dice_list.count(dice_list[0]) >= 4:
            return 4 * dice_list[0]
        elif dice_list.count(dice_list[1]) >= 4:
            return 4 * dice_list[1]
        else:
            return 0

    def little_straight_func(dice_list):
        if set(dice_list) == {1, 2, 3, 4, 5}:
            return 30
        else:
            return 0

    def big_straight_func(dice_list):
        if set(dice_list) == {2, 3, 4, 5, 6}:
            return 30
        else:
            return 0

    def choice_func(dice_list):
        return sum(dice_list)

    switcher = {
        YACHT: yacht_func,
        ONES: ones_func,
        TWOS: twos_func,
        THREES: threes_func,
        FOURS: fours_func,
        FIVES: fives_func,
        SIXES: sixes_func,
        FULL_HOUSE: full_house_func,
        FOUR_OF_A_KIND: four_kind_func,
        LITTLE_STRAIGHT: little_straight_func,
        BIG_STRAIGHT: big_straight_func,
        CHOICE: choice_func
    }

    func = switcher.get(category)
    result = func(dice)
    return result


