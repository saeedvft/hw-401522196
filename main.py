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
        n = str(self.n) 
        # sums = sum([i * j if i * j < 10 else j * i - 9 for i, j in ((int(x), int(y)) for x, y in zip(n, '21' * 8))]) 
        sums = 0 
        for i, j in zip(n, '21'*8): 
            l = int(i)*int(j) 
            if (l) > 9: 
                l -= 9 
            sums += l 
        return not sums % 10 
 
    def id_bank(self): 
        id = str(self.n)[:6] 
        self.ids = {} 
        soup = BeautifulSoup(get('https://www.elmefarda.com/پیش-شماره-کارت-بانکی/').text, 'html.parser') 
        box = soup.select('table tr td') 
        for i, j in zip(box[1::2], box[::2]): 
            self.ids[i.text] = j.text 
        bank = self.ids.get(id, None) 
        if bank: 
            return bank 
        self.valid = False 
        return None 
 
    def generator(self, this_bank=True):
        pass