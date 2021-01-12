
"""
1) 
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. 
If Bob is not in the array, return -1. 
"""


def csWhereIsBob(names):
    # iterate over the names list to look fot Bob
    if('Bob' in names):

        # if Bob is found, return the index of Bob
        return names.index('Bob')

    return -1


"""
2 ) 
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.
"""


def csAlphanumericRestriction(input_str):
    # iterate over the input strings looking for number or letter
    if (input_str.isdigit()) or (input_str.isalpha()):
        # if string is only letter return true
        # if string is only number return true
        return True
    else:
        return False

    # otherwise return False

"""
3 ) 
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.

"""

def csOppositeReverse(txt):
    #  iterate over strings
    # swap the case lower -> upper and opposite
    swapped = txt.swapcase()
    # split the letter into array
    word = txt.split()
    # reverse the array
    reverse = swapped[::-1]
    
    # joined array back to string
    return("".join(reverse))

"""
4 )
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
"""

def csSquareAllDigits(n):
    # goes over all the numbers
    # changing interger that pass in to the string
    # going over the array and squaring each number 
    # joining the array back into string
    squared = "".join(str(int(i)**2) for i in str(n))
    #  changing the string back to interger
    interger = int(squared)
    return interger


"""
5 ) 
Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
"""

def csSchoolYearsAndGroups(years, groups):
    letter = ''
    for i in range(1, years+1):
        for j in range(groups):
            if(i == years and j == groups-1):
                letter += str(i) + chr(97+j)
                return letter
            letter += str(i) + chr(97+j) + ', '

"""
6 ) 
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:
"""

def csMakeItJazzy(chords):
    # we are stating 7 into a variable
    num = 7 
    #  creating empty list for use later 
    lst = []
    # we want to iterate over every chord
    for chord in chords:
        # for each chord that does not have 7 in it 
        if '7' not in chord:
            lst.append(chord + str(num))
        else:
            # other will just append chord to the list 
            lst.append(chord)
            
    return lst