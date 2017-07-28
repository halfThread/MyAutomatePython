#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: guessTheNumber.py
@time: 2017/7/11 15:25
"""
import random


# 猜数字
def func():
    secret_number = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break  # this number is the correct guess!

    if guess == secret_number:
        print('Good job! You guesses is the correct guess!')
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number))


# collatz 序列
def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(str(number))
    return number


def collatzStart():
    try:
        print("Please enter number:")
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Please enter an integer!")


# class Main():
#     def __init__(self):
#         pass
#

if __name__ == '__main__':
    # func()
    collatzStart()
