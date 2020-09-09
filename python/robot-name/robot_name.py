import random


class Robot:
    names = []

    @staticmethod
    def get_random_letter_char():
        random_int = random.randint(ord('A'), ord('Z'))
        return chr(random_int)

    @staticmethod
    def get_random_digit_char():
        return str(random.randint(0, 9))

    @classmethod
    def get_new_name(cls):

        while True:
            name = ''
            for i in range(2):
                name += cls.get_random_letter_char()
            for i in range(3):
                name += cls.get_random_digit_char()

            if name not in cls.names:
                cls.names.append(name)
                return name

    def __init__(self):
        self.name = self.get_new_name()

    def reset(self):
        new_name = self.get_new_name()
        self.names.remove(self.name)
        self.name = new_name

