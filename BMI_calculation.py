#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:16:14 2019

@author: Kirsten
"""

# ask user for his/her name, weight and height
user_name = input("what is your name? ")
weight = int(input("what is your weight in kg? "))
height = float(input("what is your height in m? "))

# calculate BMI and communicate to user
BMI = weight / height**2
print(f"\nHello {user_name}!\nYour BMI is {BMI:.1f}")
