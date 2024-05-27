#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

number=random.randint(1, 101)

def guessing_game():
    #Computer picks a number between 1 & 100
    number
    
    #Ask user to take a guess as INPUT
    print("Guess a number bertween 1 - 100, NOW!\n")
    guess = input("No decimels, Wise Guy...\n")
    
    while True:
        #Check if user was correct
        if int(guess) < number:
            print(f"{guess} Is To Low...")
            guess = input("Guess Again! \n")
        elif int(guess) > number:
            print(f"{guess} Is To High...")
            guess = input("Guess Again! \n")
        elif int(guess) == number:
            print(f"{guess} Was Just Right!")
            return()
        else:
            print("Input is invalid. Check yourself!")
            guess = input("Guess Again! \n")
        
#START GAME            
guessing_game()

"""
Created on Mon May 27 14:58:15 2024

@author: tj
"""

