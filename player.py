#coding=utf-8
import os
import random
import sys
from hero import Hero, HeroRegister

class Player:
    def __init__(self, owner):
        hero_pool = HeroRegister()
        random.shuffle(hero_pool)
        self.card = hero_pool[:5]
        self.pool = hero_pool[5:]
        self.valid = 5
        self.owner = owner

    def move(self, bm):
        if self.valid == 0:
            return
        pos = random.randint(0, 4)
        while self.card[pos % 5].name == "":
            pos += 1
        
        ind = random.randint(0, bm.width * bm.height - 1)
        while bm.board[(ind % bm.total_grid) // bm.height][ind % bm.height].name:
            ind += 1
        
        self.valid -= 1
        bm.valid -= 1
        bm.cur_posx = (ind % bm.total_grid) // bm.height
        bm.cur_posy = ind % bm.height
        bm.board[bm.cur_posx][bm.cur_posy], self.card[pos % 5] = self.card[pos % 5], bm.board[bm.cur_posx][bm.cur_posy]
        bm.board[bm.cur_posx][bm.cur_posy].owner = self.owner


if __name__ == "__main__":
    x = Player()
    for item in x.card:
        print(item.attributes())

