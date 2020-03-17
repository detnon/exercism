def recite(start_verse, end_verse):
    verses = [["first", "and a Partridge in a Pear Tree."],
              ["second", "two Turtle Doves, "],
              ["third", "three French Hens, "],
              ["fourth", "four Calling Birds, "],
              ["fifth", "five Gold Rings, "],
              ["sixth", "six Geese-a-laying, "],
              ["seventh", "seven Swans-a-Swimming", ],
              ["eighth", "eight Maids-a-Milking"],
              ["ninth", "nine Ladies Dancing, "],
              ["tenth", "ten Lords-a-Leaping, "],
              ["eleventh", "eleven Pipers Piping, "],
              ["twelfth", "twelve Drummers Drumming, "]]

    output =  f"On the {verses[start_verse-1][0]} day of Christmas" \
        " my true love gave to me:"

    gifts = ""

    if start_verse and end_verse < 2:
        return output + f"{verses[0][1]}".replace("and a"," a")

    for r in range(start_verse -1, end_verse -1):
        gifts + verses[r][0]

    return output + gifts

print(recite(1,2))
