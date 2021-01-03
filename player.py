#coding=utf-8
import os
import random
import sys
from hero import Hero, HeroRegister

class Player:
    def __init__(self, owner):
        hero_pool = HeroRegister()
        for h in hero_pool:
            h.owner = owner

        #self.card = []
        #self.card.append(Hero("冰锥法师", "中立", 2, [4, 4, 3, 5], [1, 1, 1, 0], ["生物", "人类", "法师"], ["洞穿", "帷幕"]));
        #self.card.append(Hero("沙原巨蛇", "中立", 2, [5, 6, 5, 5], [0, 0, 0, 1], ["生物", "巨蛇"], ["灵动"]));
        #self.card.append(Hero("虚空幽灵", "中立", 2, [4, 3, 4, 3], [1, 0, 0, 1], ["生物", "幽魂"], ["侵扰3", "躲闪"]));
        #self.card.append(Hero("治安骑士团", "中立", 2, [3, 6, 6, 6], [1, 0, 1, 1], ["生物", "人类", "骑士"], ["警戒", "护卫"]));
        #self.card.append(Hero("岩土元素", "中立", 1, [6, 6, 6, 6], [1, 1, 0, 0], ["生物", "元素"], ["坚韧1"]));
        #for h in self.card:
        #    h.owner = owner
        #self.pool = []
        #self.pool.append(Hero("山脊幼龙", "中立", 1, [6, 5, 5, 6], [0, 1, 1, 0], ["生物", "龙"], ["烈焰1"]));
        #self.pool.append(Hero("精良射手", "中立", 1, [5, 4, 5, 5], [0, 0, 1, 1], ["生物", "人类"], ["箭矢"]));
        #self.pool.append(Hero("赛场公牛", "中立", 1, [3, 6, 2, 6], [1, 1, 1, 1], ["生物", "牛"], ["践踏"]));
        #self.pool.append(Hero("血口黏垢", "中立", 1, [7, 7, 7, 7], [0, 0, 1, 1], ["生物", "流浆"], ["吞食"]));
        #self.pool.append(Hero("骷髅勇士", "中立", 1, [4, 4, 4, 4], [1, 1, 1, 1], ["生物", "骷髅", "战士"], ["损毁"]));
        #self.pool.append(Hero("钢指魔像", "中立", 1, [6, 3, 3, 6], [0, 1, 0, 0], ["器械", "魔像"], ["洞穿"]));
        #self.pool.append(Hero("苔地巨魔", "中立", 1, [6, 6, 6, 6], [0, 0, 1, 1], ["生物", "巨魔"], ["警戒"]));
        #self.pool.append(Hero("塔楼石像鬼", "中立", 1, [5, 3, 4, 4], [0, 1, 1, 0], ["生物", "石像鬼"], ["惊骇1"]));
        #self.pool.append(Hero("矿区工人", "中立", 1, [3, 5, 4, 3], [1, 0, 1, 1], ["生物", "人类"], ["探索1"]));
        #self.pool.append(Hero("荒野巨人", "中立", 0, [2, 3, 7, 6], [1, 1, 0, 1], ["生物", "巨人"], []));
        #self.pool.append(Hero("前线士兵", "中立", 0, [5, 5, 5, 5], [0, 0, 0, 0], ["生物", "人类", "战士"], []));
        #self.pool.append(Hero("受雇打手", "中立", 0, [6, 6, 3, 3], [1, 1, 0, 1], ["生物", "人类"], []));
        #self.pool.append(Hero("惊魂木乃伊", "中立", 0, [6, 3, 6, 4], [0, 1, 1, 1], ["生物", "灵俑"], []));
        #for h in self.pool:
        #    h.owner = owner
        #self.play_nums = 0

        random.shuffle(hero_pool)
        self.card = hero_pool[:5]
        self.pool = hero_pool[5:]
        self.owner = owner

    def valid(self):
        return len(list(filter(lambda x: x.name != "", self.card)))

    def get_valid_card_index(self):
        index = []
        for i, c in enumerate(self.card):
            if c.name:
                index.append(i)
        return index

    def move(self, bm, enemy):
        #if self.owner == "Red":
        #    seq = [1, 3, 4, 2, 6]
        #else:
        #    seq = [5, 7, 0, 8, 4]
        #pos = self.play_nums
        #ind = seq[pos]
        #self.play_nums += 1

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
        return self.card[card_pos], card_pos, bm_curx, bm_cury

if __name__ == "__main__":
    x = Player()
    for item in x.card:
        print(item.attributes())

