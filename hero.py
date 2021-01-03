#coding=utf-8
import copy
import os
import random
import sys

class Hero:
    def __init__(s, name="", camp="", quality=0, dimentions=[0,0,0,0], green=[0,0,0,0], species=[], skill=[]):
        s.name = name
        s.camp = camp
        s.quality = quality
        s.owner = ""
        s.order = -1
        s.try_flip_num = 0
        s.green = green
        s.species = set(species)
        s.skill = set(skill)
        s.true_dimentions = copy.copy(dimentions)
        s.dimentions = [d + random.randint(0, g) for d, g in zip(dimentions, green)]

    def attributes(s):
        return "%s, 阵营:%s, 品质:%s, 所属:%s, 四维:%s, 绿点%s, 物种:%s, 技能:%s"%\
                (s.name, s.camp, s.quality, s.owner, s.dstr(s.dimentions), s.dstr(s.green), s.sstr(s.species), s.sstr(s.skill))

    def dstr(s, x):
        return "L%d-R%d-U%d-D%d"%(x[0],x[1],x[2],x[3])

    def sstr(s, x):
        return '-'.join(x)

    def clear(s):
        s.name = ""
        s.camp = ""
        s.quality = 0
        s.owner = ""
        s.order = -1
        s.try_flip_num = 0
        s.dimentions = [0, 0, 0, 0]
        s.green = [0, 0, 0, 0]
        s.species = set()
        s.skill = set()

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
    return HerosPool

if __name__ == "__main__":
    pool = HeroRegister()
    for item in pool:
        print(item.attributes())
