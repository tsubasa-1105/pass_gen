# -*- coding: utf-8 -*-
import secrets

class PassGen:

    def __init__(self,size=12,upper=False,digits=False,sign=False):

        self.__lower  = 'abcdefghijklmnopqrstuvwxyz'
        self.__upper  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__digits = '0123456789'
        self.sign   = '`˜!@#$%^&*()_+-={}[]\|:;"\'<>,.?/'
        self.size   = size
        self.__flg  = 0
        self.__set(0,upper)
        self.__set(1,digits)
        self.__set(2,sign)
    
    def __get(self,i):
        return (self.__flg&(1<<i)) >> i
    
    def __set(self,i,flg):
        if flg: self.__flg = self.__flg | (1<<i)
        else: self.__flg = self.__flg & ~(1<<i)
    
    def set_upper(self,flg):
        self.__set(0,flg)

    def set_digits(self,flg):
        self.__set(1,flg)

    def set_sign(self,flg):
        self.__set(2,flg)
    
    def generate(self,size=None):
        s = self.size if not size else size
        w = self.__lower*5
        if self.__get(0): w += self.__upper
        if self.__get(1): w += self.__digits
        if self.__get(2): w += self.sign
        return ''.join([secrets.choice(w) for _ in range(s)])

if __name__ == "__main__":

    # 数字と記号を含んだ18桁のパスワード生成
    pg = PassGen(size=18,digits=True,sign=True)
    pw = pg.generate()
    print('pw ->',pw)

    # 9バイトのトークンを生成
    to = secrets.token_hex(9)
    print('to ->',to)