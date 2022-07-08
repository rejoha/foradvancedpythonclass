import black

print("Hello world")

# Script to check if variable is odd or even
x = 3

if (x % 2) == 0:
    even = True
else:
    even = False

even


# Function


def funct(x):
    y = x + 1
    a = "Wohoo"
    return y, a


z = funct(2)

z[1]

# Function to check if variable is odd or even


def odd_or_even(x):
    """Function to test for odd or even numbers"""
    try:
        # Checks the value and returns true or false based on results
        if (x % 2) == 0:
            even = True
        else:
            even = False
        return even
    except:  # If input is not a number, return invalid
        return "invalid input"


# Fibonacci sequence


def fibonacci(r):
    o = range(r)
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in o:
        x = n1 + n2
        print(x)
        n1 = n2
        n2 = x


fibonacci(10)


string = "Hello world"


def transform_string(string, encode):
    """Transform each letter into the next letter in the alphabet.
    Other symbols/spaces remain the same, and the last letter of the alphabet becomes the first letter."""
    if encode == True:
        trans = 1
        end = 0
    else:
        trans = -1
        end = -1
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    new_string = ""
    for l in string:
        if l.lower() in alphabet:
            try:
                i = alphabet.index(l.lower())
                new_string += alphabet[i + trans]
            except IndexError:
                new_string += alphabet[end]
        else:
            new_string += l

    return new_string


transform_string("This is a test!!! zzz aaa", True)


import this
