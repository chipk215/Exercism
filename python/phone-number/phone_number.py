import re


class PhoneNumber:
    pattern = re.compile(r"^(?:\+?1[-. ]?)?\(?([2-9]{3})\)?[-. ]?([2-9]{3})[-. ]?([0-9]{4})$")

    def __init__(self, number):
        number = number.replace(" ", "")
        match = self.pattern.match(number)
        if match:
            print("Match was found at {start}-{end}: {match}".format(start=match.start(), end=match.end(),
                                                                     match=match.group()))
            self.area_code = match.group(1)
            self.exchange = match.group(2)
            self.subscriber = match.group(3)
            self.number = self.area_code + self.exchange + self.subscriber
            print(f"{self.area_code}  {self.exchange}  {self.subscriber}")
        else:
            raise ValueError("Number dosn't match pattern")

    def pretty(self):
        return f"({self.area_code})-{self.exchange}-{self.subscriber}"


if __name__ == "__main__":
    result = PhoneNumber("(223) 456-7890")
    print(result.number)
    print(result.pretty())
