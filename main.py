from functions import *


# Start Screen
term_clear()
print('#' * 32)
print("What do you want information on?\n")
ls_options()



while True:
    print('#' * 32)
    print("""
Enter a number  ||  'l' to show list again  ||  'c' to clear screen  ||  'q' to quit
          """)
    
    user = input(">>> ")
    print('#' * 5)
    term_clear()
    if user.lower() == 'q':
        break
    elif user.lower() == 'c':
        term_clear()
        continue
    elif user.lower() == 'l':
        print('')
        ls_options()
    elif user == '0':
        integers()
        floats()
        strings()
        booleans()
        lists()
        tuples()
        dictionaries()
        math()
        operators()
    elif user == '1':
        integers()
    elif user == '2':
        floats()
    elif user == '3':
        strings()
    elif user == '4':
        booleans()
    elif user == '5':
        lists()
    elif user == '6':
        tuples()
    elif user == '7':
        dictionaries()
    elif user == '8':
        math()
    elif user == '9':
        operators()
    else:
        print("*** INVALID INPUT ***")
    
    print('')
    