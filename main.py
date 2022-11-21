from ctypes import ArgumentError 
from requests import get 
from bs4 import BeautifulSoup 
from random import choice, randint 
 
 
class Card: 
    def __init__(self, number=10**15) -> None: 
        if len(str(number)) != 16 or type(number) != int: 
            raise ArgumentError('Number should be an inetger with 16 digits.') 
        self.n = number 
        self.valid = self.check() 
        self.bank = self.id_bank() 
 
    def check(self) -> bool:
        pass