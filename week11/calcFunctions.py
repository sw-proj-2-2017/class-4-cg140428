from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r + "(2)"

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    """        1 I
            5 V
            10 X
            50 L
            100 C
            500 D
            1000 M
        """
    try:
        n = int(numStr)
        if n >= 4000:
            return 'Error!'
        romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        result = ''
        for value, letters in romans:
            while n >= value:
                result += letters
                n -= value
        return result
    except:
        result = 'Error!'
    return result


def romanToDec(numStr):
    roman_result = numStr
    N = 0
    romans1 = [
        ('CM', 900), ('CD', 400),
        ('XC', 90), ('XL', 40),
        ('IX', 9), ('IV', 4),
    ]
    romans2 = [
        ('M', 1000), ('D', 500),
        ('C', 100), ('L', 50),
        ('X', 10), ('V', 5),
        ('I', 1)
    ]

    for key, value in romans1:
        if roman_result.find(key) != -1:
            key_list = roman_result.split(key)
            key_num = len(key_list) - 1
            roman_result = ''.join(key_list)
            N += key_num * value

    for key, value in romans2:
        if roman_result.find(key) != -1:
            key_list = roman_result.split(key)
            print(key_list)
            key_num = len(key_list) - 1
            roman_result = ''.join(key_list)
            N += key_num * value
    result = N

    return result
