#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

number=random.randint(1, 101)

def guessing_game():
    #Computer picks a number between 1 & 100
    number
    
    chances = 3
    
    #Ask user to take a guess as INPUT
    print("Guess a number bertween 1 - 100...\n You Only Have 3 Chances!!!\n")
    guess = input("No Decimels, Archimedes...\n")
    
    while chances >= 2:
        #Check if user was correct
        if int(guess) < number:
            print(f"{guess} Is To Low...")
            chances -= 1
            guess = input(f"Guess Again!\n You have {chances} chance left\n")
        elif int(guess) > number:
            print(f"{guess} Is To High...")
            chances -= 1
            guess = input(f"Guess Again!\n You have {chances} chance left\n")
        elif int(guess) == number:
            print(f"{guess} Was Just Right!")
            return()
        else:
            print("Input is invalid. Check yourself!")
            guess = input(f"Guess Again! You have {chances} left\n")
        print("You Lose Out Of Guesses")
    return()
        
#START GAME            
guessing_game()

"""
Created on Mon May 27 14:58:15 2024

@author: tj
"""

