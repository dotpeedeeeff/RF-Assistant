
def find_letter(input: str) -> str:
    input = float(input)

    mega = input / 1E6
    kilo = input / 1000

    if mega >= 1:
        letter = "M"

    elif kilo >= 1:
        letter = "k"

    else:
        letter = "R"

    return letter


def find_ohm(input: str, letter: str) -> str:

    suffix = {
        "M": 1E6,
        "k": 1E3,
        "R": 1
    }

    input = float(input)
    start = input / suffix[letter]

    if 1000 > start >= 10:
        first = start / 10
        first = int(first)
        first = str(first)

        second = start /10
        second = second % 1
        second = round(second, 1)
        second = second * 10
        second = int(second)
        second = str(second)

        return first + second + letter

    elif 10 > start > 1:
        first = int(start)
        first = str(first)
        second = start % 1
        second = round(second, 1)
        second = second * 10
        second = int(second)
        second = str(second)

        if second == "0":
            second = ""

        return first + letter + second

    elif start == 1:
        start = int(start)
        start = str(start)
        return start + letter


def resistance_converter(input: str) -> str:
    suffix = find_letter(input)
    return find_ohm(input, suffix)

