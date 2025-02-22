class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        val = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        roman_numeral = ""
        num = self.number
        for arabic, roman in val:
            while num >= arabic:
                roman_numeral += roman
                num -= arabic
        return roman_numeral

num = int(input("Enter an integer: "))
converter = IntegerToRoman(num)
print(f"Roman numeral: {converter.convert()}")
