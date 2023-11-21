#!/usr/bin/env python3

def happy_new_year():
    for countdown in range(10, 0, -1):
        print(countdown)
    
    print("Happy New Year!")

    # code goes here!
    

def square_integers(int_list):
    # code goes here!
        square_integers=[integer ** 2 for integer in int_list]
        return square_integers

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
