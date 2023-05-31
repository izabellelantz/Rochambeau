"""
class Player which holds player information to be used in game.
"""


class Player:
   def __init__(self, f_name):
       self.first_name = f_name


   def is_valid_name(self, f_name):
       alphabet = 'abcdefghijklmnopqrstuvwxyz'
       for letter in f_name:
           try:
               letter.lower() in alphabet
           except ValueError:
               raise ValueError('Invalid name!')
           self.first_name = f_name


   def __str__(self):
       return f'{self.first_name}'
