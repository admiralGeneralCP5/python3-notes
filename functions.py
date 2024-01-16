import os
import platform

sections = ['All', 'Integers', 'Floats', 'Strings', 'Booleans', 'Lists', 'Tuples', 'Dictionaries', 'Math', 'Operators']


def ls_options():
    counter = 0
    for i in sections:
        print(counter, '--', i, '\n')
        counter += 1


def term_clear():
    opsys = platform.system()
    if opsys == 'Darwin' or opsys == 'Linux':
        os.system("clear")
    elif opsys == 'Windows':
        os.system("cls")


# Note Data Below

def integers():
    info = """
Integers:
        - any whole number positive or negative
        - int() takes input and then returns it as an integer
"""
    print(info)


def floats():
    info = """
Floats:
        - floating point numbers
        - numbers with a decimal
        - float() takes input and then returns it as a float; 10 becomes 10.0
"""
    print(info)


def strings():
    info = """
Strings:
    - any character in quotations
    - are iterable, character by character
    - characters are indexed
    - triple double quotes allows a string to span multiple lines
    - single or double quotes for everything else
    - str() takes input and then returns it as a string
    - len() returns the number or characters within the string
    Escape Character:
        - "\\" is the escape character (backslash)
        - using the escape character allows double quotes to be within a string
            example: print("\\"Hello there.\\"")
            output:  "Hello there."
        - \\n adds a new line
    Formatted String:
        - prefix an 'f' before the quotes of a string to make it a formatted string
        - this allows variables to be called and expressions to be entered within the string using {}
            example: name = 'Johhn'
                    print(f"Hello {name}.")
            output:  Hello John.
    .format String:
        - older way to use variables and expressions within a string
            example: name = 'John'
                    age = 42
                    print({0} is {1} years old.".format(name, age))
            output:  John is 42 years old.
        - the {} can be left empty or indexes can be used as seen in the example
        - using indexes allows a variable to be used multiple times
    % Formatting:
        - another old way to use variables and expressions within a string
            example: name = 'John'
                    age = 42
                    print("%s is %d years old." % (name, age))
            output:  John is 42 years old.
        - %s for strings
        - %d for integers
    Methods:
        - .upper() returns a string that is all upper case
        - .lower() returns a string that is all lower case
        - .title() returns a string in which the first letter in every word is upper case
        - .strip() returns a string with white spaces removed on both sides
        - .lstrip() .rstrip() removes white spaces on either the left or righ side
        - .find() returns the index of specified characters within the string, -1 if the characters are not there
        - .replace() 
"""
    print(info)


def booleans():
    info = """
Booleans:
        - true or false
        - bool() takes input and returns the boolean value
        - 0 is false while all other numbers are true
        - emtpy strings and 'None' are also false
"""
    print(info)


def lists():
    info = """
Lists:
   
    - are defined using []
    example: numbers = [1, 2, 3, 4]
    - items are sorted by index starting at 0
    - enumerate() returns a tuple with the index and value of the item

    Adding/Inserting Items:
        - .append() add item to the end of the Lists
        - .insert() inserts an item at any index; example: .insert(3, 'two')  # inserts 'two' at index 3

    Removing Items:
        - .pop() removes item at the end of the list unless an index is specified
        - .remove() remove the first occurence of whatever thing is specified
        - .clear() removes all of the items

    Finding Items:
        - .index() returns the index of the input, will return an error if the item does not exist
        - .count() returns the number of times something exist within the list

    Sorting:
        - .sort() and sorted() sorts in ascending order; reverse=True will change it to descending
"""
    print(info)


def tuples():
    info = """
Tuples:

    - can be defined with () or a trailing ,
      example: tuple1 = (2, 3)
               tuple2 = 4,
    - items cannot be added or removed; immutable
    - can be concatenated
    - items are indexed
"""
    print(info) 


def dictionaries():
    info = """
Dictionaries:
    - are collections of key value pairs
    - can be defined by
      example: dictOne = {'x': 1, 'y': 2}
               dictTwo = dict(x=1, y=2)
    - both methods shown in the example create the same dictioanary
    - items cannot be looked up by numerical indexes
    - keys are used to access values
      example: dictOne['x']
      output:  1
    - keys can be reassigned vlaues; if the key does not exist a new key pair will be created
      example: dictOne['y'] = 7
               dictOne['z'] = 3
               print(dictOne)
      output:  {'x': 1, 'y': 7, 'z': 3}
    
    .get():
        - returns the value of a key
          example: print(dictTwo.get('x'))
          output:  1
        - will return 'None' if the key does not exist; a default value can be specified
          example: dictTwo.get('w', 0)  # if 'w' does not exist '0' will be returned

    .values():
        - returns a list of the values for every key
        - using list() will clean up the results

    .keys():
        - returns alist of all of the keys
        - using list() will clean up the results

    .pop():
        - removes a key value pair
        - will take the value of the key being removed
          example: value = dictTwo.pop('y')  # 'y' will be removed and 'value' will be assigned its value
"""
    print(info)


def math():
    info = """
Math:

    Division:
        - / returns a float
        - // returns an integer
        - % returns the modulous (the remainder in Division)

    Exponent:
        example: 2**3  # 2 to the power of 3
        output:  8

    Basic Functions:
        - round() rounds the number to the closest integer unless a second number is entered to specify decimal places
        - abs() returns the absolute value

    Complex Numbers:
        - are imaginary numbers in Math
        - are represented as 'j' in Python while in math they are represented as 'i'
"""
    print(info)


def operators():
    info = """
Operators:

    Logical:
        - and
        - or
        - not

    Comparison:
        - <
        - <=
        - >
        - >=
        - == equal to
        - != not equal to

    Chained Comparison:
        example: 18 <= age < 65
        - the example would replace; age >= 18 and age < 65
"""
    print(info)