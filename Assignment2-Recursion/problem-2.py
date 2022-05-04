# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
return a list of all letter combinations they could have been trying to type on the keypad.

Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]
"""

### FIRST THOUGHTS ###
"""
Recursivly, we can continue seperating each digit until we hit the end of our string of digits.  We can utilize a
switch case to determine what letters to output and a stack-like implementation to determine the order of output.
"""

### SUDO CODE ###
"""
Take the last character in the string.
Use a switch statement to determine the different letter combinations.
Recursivly loop through the first steps until all the letters have been processed.
Generate all letter combinations in the opposite order that the characters were processed.
Append them to a list and return.
"""

### CODE ###
def numbersToChar(argument):
    switcher = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    return switcher.get(argument)

def letterCombinations(digits, combo, origin_len, combinations):
    if origin_len == 0:
        combinations.append(combo)
        return
    for char in numbersToChar(digits[0]):
        combo1 = combo + char
        letterCombinations(digits[1:], combo1, origin_len-1, combinations)
    return combinations

def t9_letters(digits):
    combinations = []
    if len(digits) == 0:
        return []
    letterCombinations(digits, '', len(digits), combinations)
    return combinations

### TEST CODE ###
print(t9_letters("23"))
print(t9_letters("4663"))