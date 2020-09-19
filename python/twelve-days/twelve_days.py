
lyrics = {1: ('first', "a Partridge in a Pear Tree"),
          2: ('second', "two Turtle Doves"),
          3: ('third', "three French Hens"),
          4: ('fourth', "four Calling Birds"),
          5: ('fifth', "five Gold Rings"),
          6: ('sixth', "six Geese-a-Laying"),
          7: ('seventh', "seven Swans-a-Swimming"),
          8: ('eighth', "eight Maids-a-Milking"),
          9: ('ninth', "nine Ladies Dancing"),
          10: ('tenth', "ten Lords-a-Leaping"),
          11: ('eleventh', "eleven Pipers Piping"),
          12: ('twelfth', "twelve Drummers Drumming")}


def recite_verse(number):
    nth = lyrics[number][0]
    verse = f"On the {nth} day of Christmas my true love gave to me: "
    while number > 0:
        if number == 1:
            verse += lyrics[number][1] + '.'
        elif number == 2:
            verse += lyrics[number][1] + ', and '
        else:
            verse += lyrics[number][1] + ', '
        number -= 1

    return verse


def recite(start_verse, end_verse):
    result = []
    for verse_number in range(start_verse, end_verse+1):
        result.append(recite_verse(verse_number))

    return result

