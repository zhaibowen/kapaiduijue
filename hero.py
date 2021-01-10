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
        s.green = green
        s.species = set(species)
        s.skill = {}
        for sk in skill:
            s.skill[sk] = 0
        s.dimentions = [d + random.randint(0, g) for d, g in zip(dimentions, green)]

    def attributes(s):
        return "%s, 阵营:%s, 品质:%s, 所属:%s, 四维:%s, 绿点:%s, 物种:%s, 技能:%s"%\
                (s.name, s.camp, s.quality, s.owner, s.dstr(s.dimentions), s.dstr(s.green), s.sstr(s.species), s.sstr(s.skill))

    def dstr(s, x):
        x = list(x)
        return "L%d-R%d-U%d-D%d"%(x[0],x[1],x[2],x[3])

    def sstr(s, x):
        return '-'.join(x)

    def clear(s):
        s.name = ""
        s.camp = ""
        s.quality = 0
        s.owner = ""
        s.order = -1
        s.dimentions = [0, 0, 0, 0]
        s.green = [0, 0, 0, 0]
        s.species = set()
        s.skill = {}

if __name__ == "__main__":
    pass
