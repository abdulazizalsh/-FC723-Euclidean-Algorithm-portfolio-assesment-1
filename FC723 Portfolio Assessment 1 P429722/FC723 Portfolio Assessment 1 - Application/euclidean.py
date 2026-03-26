# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:41:02 2026

@author: abdul
"""

def calculate_gcd(number_1, number_2): 
    while number_2 != 0: 
        #we are looping the program until number 2 equals to 0.
        
        remainder = number_1 % number_2   
        #remainder takes the remaining number.
        number_1 = number_2  
        # replaces the variable “number_1” with “number_2”.
        number_2 = remainder   
        #replaces the variable “number_2” with "remainder”
    return number_1  #returns the gcd

#test variables
first_number = 33
second_number = 9

result = calculate_gcd(first_number, second_number) #send the numbers and fetches the gcd
print("GCD result >>", result) #prints the result
