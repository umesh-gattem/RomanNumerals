roman_numeral_map = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)

def integer_to_roman(number):
    if not (0 < number < 4000):
        raise Exception("Range should be between 0 to 3999")
    if not isinstance(number,int):
        raise "Only integers are accepted"
    result = ''
    for roman, integer in roman_numeral_map :
        while number >= integer:
            result += roman
            number -= integer
    return result

if __name__ == "__main__":
    print("okay")