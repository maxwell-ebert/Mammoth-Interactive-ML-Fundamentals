# -*- coding: utf-8 -*-
"""02 Combinatorics for Probability.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yNsxpR0HMizrj8VEI5ROp13iVdy_BAv0

#  Combinatorics for Probability

https://colab.research.google.com
"""

from math import factorial 

def calculate_probability(n, k):

  n_choose_k = factorial(n)/(factorial(k)*factorial(n-k)) 

  probability = n_choose_k / 2**n

  return probability

number_of_coin_flips = 5 

number_of_head_flips = 0

calculate_probability(number_of_coin_flips, number_of_head_flips)

calculate_probability(number_of_coin_flips, 1)

calculate_probability(number_of_coin_flips, 2)

calculate_probability(number_of_coin_flips, 3)

calculate_probability(number_of_coin_flips, 4)

calculate_probability(number_of_coin_flips, 5)