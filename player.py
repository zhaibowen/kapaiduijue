#coding=utf-8
import curses
import os
import random
import sys
from hero import Hero

def HeroRegister():
    HerosPool = []
    HerosPool.append(Hero("前线士兵", "中立", 0, [5, 5, 5, 5], [0, 0, 0, 0], ["生物", "人类", "战士"], []));
    HerosPool.append(Hero("林地野狼", "中立", 0, [4, 4, 5, 5], [1, 1, 1, 1], ["生物", "野兽", "狼"], []));
    HerosPool.append(Hero("荒野巨人", "中立", 0, [2, 3, 7, 6], [1, 1, 0, 1], ["生物", "巨人"], []));
    HerosPool.append(Hero("受雇打手", "中立", 0, [6, 6, 3, 3], [1, 1, 0, 1], ["生物", "人类"], []));
    HerosPool.append(Hero("惊魂木乃伊", "中立", 0, [6, 3, 6, 4], [0, 1, 1, 1], ["生物", "灵俑"], []));
    HerosPool.append(Hero("赛场公牛", "中立", 1, [3, 6, 2, 6], [1, 1, 1, 1], ["生物", "牛"], ["践踏"]));
    HerosPool.append(Hero("矿区工人", "中立", 1, [3, 5, 4, 3], [1, 0, 1, 1], ["生物", "人类"], ["探索1"]));
    HerosPool.append(Hero("苔地巨魔", "中立", 1, [6, 6, 2, 3], [0, 0, 1, 1], ["生物", "巨魔"], ["警戒"]));
    HerosPool.append(Hero("塔楼石像鬼", "中立", 1, [5, 3, 4, 4], [0, 1, 1, 0], ["生物", "石像鬼"], ["惊骇1"]));
    HerosPool.append(Hero("钢指魔像", "中立", 1, [6, 3, 3, 6], [0, 1, 0, 0], ["器械", "魔像"], ["洞穿"]));
    HerosPool.append(Hero("精良射手", "中立", 1, [7, 3, 6, 2], [0, 0, 1, 1], ["生物", "人类"], ["箭矢"]));
    HerosPool.append(Hero("岩土元素", "中立", 1, [5, 5, 5, 5], [1, 1, 0, 0], ["生物", "元素"], ["坚韧1"]));
    HerosPool.append(Hero("骷髅勇士", "中立", 1, [4, 4, 4, 4], [1, 1, 1, 1], ["生物", "骷髅", "战士"], ["损毁"]));
    HerosPool.append(Hero("血口黏垢", "中立", 1, [4, 5, 4, 4], [0, 0, 1, 1], ["生物", "流浆"], ["吞食"]));
    HerosPool.append(Hero("山脊幼龙", "中立", 1, [6, 5, 5, 6], [0, 1, 1, 0], ["生物", "龙"], ["烈焰1"]));
    HerosPool.append(Hero("治安骑士团", "中立", 2, [3, 6, 6, 3], [1, 0, 1, 1], ["生物", "人类", "骑士"], ["警戒", "护卫"]));
    HerosPool.append(Hero("冰锥法师", "中立", 2, [4, 4, 3, 5], [1, 1, 1, 0], ["生物", "人类", "法师"], ["洞穿", "帷幕"]));
    HerosPool.append(Hero("沙原巨蛇", "中立", 2, [5, 6, 5, 5], [0, 0, 0, 1], ["生物", "巨蛇"], ["灵动"]));
    HerosPool.append(Hero("虚空幽灵", "中立", 2, [4, 3, 4, 3], [1, 0, 0, 1], ["生物", "幽魂"], ["侵扰3", "躲闪"]));
    HerosPool.append(Hero("链锤魔鬼", "中立", 2, [6, 6, 5, 5], [0, 1, 1, 0], ["生物", "魔鬼"], ["连击", "变节"]));
    HerosPool.append(Hero("守猎食人花", "狂野", 2, [5, 4, 6, 2], [1, 1, 0, 1], ["生物", "植物"], ["警戒", "吞食"]));
    return HerosPool

class Player:
    def __init__(self, owner, mode='random', select_card='random', stdscr=None):
        self.owner = owner
        self.mode = mode
        self. stdscr = stdscr
        hero_pool = HeroRegister()
        for h in hero_pool:
            h.owner = owner

        if select_card == "random":
            random.shuffle(hero_pool)
            self.card = hero_pool[:5]
            self.pool = hero_pool[5:]
        elif select_card == "default":
            self.card = [
                Hero("治安骑士团", "中立", 2, [30, 60, 60, 30], [1, 0, 1, 1], ["生物", "人类", "骑士"], ["警戒", "护卫", "坚韧1"]),
                Hero("冰锥法师", "中立", 2, [40, 40, 30, 50], [1, 1, 1, 0], ["生物", "人类", "法师"], ["洞穿", "帷幕", "坚韧1"]),
                Hero("沙原巨蛇", "中立", 2, [50, 60, 50, 50], [0, 0, 0, 1], ["生物", "巨蛇"], ["灵动", "坚韧1"]),
                Hero("虚空幽灵", "中立", 2, [40, 30, 40, 30], [1, 0, 0, 1], ["生物", "幽魂"], ["侵扰3", "躲闪", "坚韧1"]),
                Hero("链锤魔鬼", "中立", 2, [60, 60, 50, 50], [0, 1, 1, 0], ["生物", "魔鬼"], ["连击", "变节", "坚韧1"]),
            ]
            for h in self.card:
                h.owner = owner
            hero_set = set(map(lambda x: x.name, self.card))
            self.pool = []
            for hero in hero_pool:
                if hero.name not in hero_set:
                    self.pool.append(hero)
        elif select_card == "select":
            self.stdscr.attron(curses.color_pair(3))
            for i, h in enumerate(hero_pool):
                self.stdscr.addstr(i, 10-len(str(i+1)), "%d %s"%(i+1, h.attributes()))
            self.stdscr.addstr(38, 70, self.owner)
            self.stdscr.refresh()
            
            hero_index = ""
            while True:
                c = self.stdscr.getch(38, 80+len(hero_index))
                if ord('0') <= c and c <= ord('9'):
                    hero_index += chr(c)
                elif c == ord(' '):
                    hero_index += chr(c)
                elif c == 127:
                    hero_index = hero_index[:-1]
                elif c == 10:
                    break
            hero_index = list(map(int, hero_index.strip().split(' ')))
            self.card, self.pool = [], []
            for i in range(5):
                self.card.append(hero_pool[hero_index[i]-1])
            for index, hero in enumerate(hero_pool):
                if index+1 not in hero_index:
                    self.pool.append(hero)

    def valid(self):
        return len(list(filter(lambda x: x.name != "", self.card)))

    def get_valid_card_index(self):
        index = []
        for i, c in enumerate(self.card):
            if c.name:
                index.append(i)
        return index

    def move(self, bm, enemy):
        if self.valid() == 0:
            return self.card[0], 0, 0, 0

        if self.mode == "random":
            pos = random.randint(0, 4)
            while self.card[pos % 5].name == "":
                pos += 1
            
            ind = random.randint(0, bm.width * bm.height - 1)
            while bm.board[ind // bm.height][ind % bm.height].name:
                ind += 1
                ind %= bm.width * bm.height
            
            card_pos = pos % 5
            bm_curx = ind // bm.height
            bm_cury = ind % bm.height
        elif self.mode == "human":
            self.stdscr.attron(curses.color_pair(3))
            self.stdscr.addstr(38, 80, "select:");
            self.stdscr.refresh()
            get_char_list = []
            while True:
                c = self.stdscr.getch(38, 88 + len(get_char_list))
                if ord('1') <= c and c <= ord('5'): 
                    get_char_list.append(c - ord('0') - 1)
                elif c == 127:
                    get_char_list.pop()
                elif c == 10 and len(get_char_list) >= 3:
                    break
            card_pos, bm_curx, bm_cury = get_char_list[:3]
        return self.card[card_pos], card_pos, bm_curx, bm_cury

if __name__ == "__main__":
    x = Player()
    for item in x.card:
        print(item.attributes())

