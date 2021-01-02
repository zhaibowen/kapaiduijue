#coding=utf-8
import curses
import os
import random
import sys
import time
from hero import Hero
from player import Player

class BattleManager:
    def __init__(s, stdscr, draw=True):
        s.width = 3
        s.height = 3
        #s.turn = random.randint(0, 1)
        s.turn = 0
        s.board = [[Hero() for j in range(s.height)] for i in range(s.width)]
        s.total_grid = s.width * s.height
        s.draw = draw
        s.stdscr = stdscr
    
    def has_place(s, red, blue):
        sumv = 0
        for i in range(s.width):
            sumv += len(list(filter(lambda x: x.name == "", s.board[i])))
        if sumv == 0:
            return False
        return red.valid() > 0 or blue.valid() > 0

    def turn_over(s):
        s.turn ^= 1

    def inference(s, red, blue, hero, posx, posy):
        targets = [[0, -1, 0, 1, 0], [0, 1, 1, 0, 0], [-1, 0, 2, 3, 0], [1, 0, 3, 2, 0]]
        caidingji = set(["警戒", "惊骇1", "探索1"])
        # 进场后
        # 优先级：惊骇1-1，警戒-3，探索1-5
        for ind, (x, y, a, b, f) in enumerate(targets):
            if 0 <= posx + x and posx + x < s.height and \
                    0 <= posy + y and posy + y < s.width and \
                    s.board[posx + x][posy + y].name and \
                    "惊骇1" in s.board[posx + x][posy + y].skill and \
                    s.board[posx + x][posy + y].owner != s.board[posx][posy].owner:
                sumd = 0
                for i in range(4):
                    s.board[posx][posy].dimentions[i] = max(0, s.board[posx][posy].dimentions[i] - 1)
                    sumd += s.board[posx][posy].dimentions[i]
                s.draw_card(s.board[posx + x][posy + y], posx + x, posy + y, color_skill=["惊骇1"]);
                s.draw_card(s.board[posx][posy], posx, posy, hightlight_dim=True);
                if sumd == 0:
                    s.board[posx][posy].clear()
                    s.draw_card(s.board[posx][posy], posx, posy)
                    return

        for ind, (x, y, a, b, f) in enumerate(targets):
            if 0 <= posx + x and posx + x < s.height and \
                    0 <= posy + y and posy + y < s.width and \
                    s.board[posx + x][posy + y].name and \
                    "警戒" in s.board[posx + x][posy + y].skill and \
                    s.board[posx + x][posy + y].owner != s.board[posx][posy].owner and \
                    s.board[posx][posy].dimentions[a] < s.board[posx + x][posy + y].dimentions[b]:
                tposx, tposy = posx + x, posy + y
                target_hero = s.board[tposx][tposy]
                s.draw_card(target_hero, tposx, tposy, color_skill=["警戒"]);
                if "坚韧1" in hero.skill:
                    s.draw_card(hero, posx, posy, color_skill=["坚韧1"]);
                    hero.skill.remove("坚韧1")
                elif "损毁" in hero.skill:
                    s.draw_card(hero, posx, posy, color_skill=["损毁"]);
                    hero.clear()
                else:
                    s.board[posx][posy].owner = s.board[posx + x][posy + y].owner
                    s.board[posx][posy].skill -= caidingji
                s.draw_card(hero, posx, posy);
                return

        if "探索1" in hero.skill:
            s.draw_card(hero, posx, posy, color_skill=["探索1"]);
            if red.valid() < 5:
                quality = hero.quality
                valid_pool = list(filter(lambda x: x.quality <= quality + 1, red.pool))
                if valid_pool:
                    target_hero = random.choice(valid_pool)
                    for pool_ind, h in enumerate(red.pool):
                        if h.name == target_hero.name:
                            break
                    for card_ind, h in enumerate(red.card):
                        if h.name == "":
                            break
                    red.pool[pool_ind], red.card[card_ind] = red.card[card_ind], red.pool[pool_ind]
                    red.pool.pop(pool_ind)
                    hero.skill.remove("探索1")
                    s.draw_card(red.card[card_ind], 4 + card_ind * 7, 15 if hero.owner == "Red" else 175)

        for ind, (x, y, a, b, f) in enumerate(targets):
            tposx, tposy = -1, -1
            # 寻找攻击目标时
            # 优先级：洞穿-4，箭矢-5
            if 0 <= posx + x and posx + x < s.height and \
                    0 <= posy + y and posy + y < s.width and \
                    s.board[posx + x][posy + y].name and \
                    s.board[posx + x][posy + y].owner != s.board[posx][posy].owner:
                tposx, tposy = posx + x, posy + y
            
            if "箭矢" in hero.skill:
                if 0 <= posx + 2 * x and posx + 2 * x < s.height and \
                        0 <= posy + 2 * y and posy + 2 * y < s.width and \
                        (s.board[posx + x][posy + y].name == "" or \
                        s.board[posx + x][posy + y].owner == hero.owner) and \
                        s.board[posx + 2 * x][posy + 2 * y].name and \
                        s.board[posx + 2 * x][posy + 2 * y].owner != s.board[posx][posy].owner:
                    tposx, tposy = posx + 2 * x, posy + 2 * y

            if tposx == -1 or tposy == -1:
                continue
            target_hero = s.board[tposx][tposy]
            if hero.dimentions[a] > target_hero.dimentions[b] or \
                    ("洞穿" in hero.skill and hero.dimentions[a] > min(target_hero.dimentions)):
                s.draw_card(hero, posx, posy, color_skill=["洞穿", "箭矢"]);
                # 进攻后
                # 优先级：吞食-5
                if "吞食" in hero.skill:
                    s.draw_card(hero, posx, posy, color_skill=["吞食"]);
                    target_hero.clear()
                    s.draw_card(target_hero, tposx, tposy);
                # 翻面前
                # 优先级：坚韧1-5，损毁-6
                elif "坚韧1" in target_hero.skill:
                    s.draw_card(target_hero, tposx, tposy, color_skill=["坚韧1"]);
                    target_hero.skill.remove("坚韧1")
                elif "损毁" in target_hero.skill:
                    s.draw_card(target_hero, tposx, tposy, color_skill=["损毁"]);
                    target_hero.clear()
                    s.draw_card(target_hero, tposx, tposy);
                else:
                    target_hero.owner = hero.owner
                    target_hero.skill -= caidingji
                    targets[ind][4] = 1
                s.draw_card(target_hero, tposx, tposy);

        # 翻面后
        # 优先级：践踏-6
        if "践踏" in hero.skill:
            s.draw_card(hero, posx, posy, color_skill=["践踏"]);
            s.stdscr.refresh()
            s.stdscr.getch()
            for x, y, a, b, f in targets:
                if f:
                    s.inference(red, blue, s.board[posx + x][posy + y], posx + x, posy + y)
        
    def get_card_num(s, owner):
        cards_num = 0
        for i in range(s.width):
            cards_num += len(list(filter(lambda x: x.owner == owner, s.board[i])))
        return cards_num

    def show_winner(s):
        s.stdscr.attron(curses.A_BOLD)
        red_cards_num = s.get_card_num("Red")
        blue_cards_num = s.get_card_num("Blue")
        if red_cards_num > blue_cards_num:
            s.stdscr.attron(curses.color_pair(1))
            s.stdscr.addstr(3, 70, "Winner is Red")
        elif red_cards_num < blue_cards_num:
            s.stdscr.attron(curses.color_pair(2))
            s.stdscr.addstr(3, 70, "Winner is Blue")
        else:
            s.stdscr.attron(curses.color_pair(3))
            s.stdscr.addstr(3, 70, "Ping Jv")
        s.stdscr.attroff(curses.A_BOLD)
        s.stdscr.refresh()
        s.stdscr.getch()

    def draw_board(s, red, blue):
        if s.draw == False:
            return
        rows, cols = s.stdscr.getmaxyx()
        s.stdscr.attron(curses.color_pair(3))
        for i in range(rows):
            s.stdscr.addstr(i, 0, " "*(cols-1))
        #s.stdscr.clear()
        for i in range(30):
            s.stdscr.addstr(5 + i, 50, "|                              |                              |                              |")
        for i in range(4):
            s.stdscr.addstr(5 + i * 10, 50, "----------------------------------------------------------------------------------------------")
        for i in range(5):
            s.stdscr.addstr(7 + i * 7, 5, "-----------------------------")
            s.stdscr.addstr(7 + i * 7, 165, "-----------------------------")

        s.stdscr.attron(curses.A_BOLD)
        if s.turn == 0:
            s.stdscr.addstr(1, 70, "Red Cards:%2d    turn: Red     Blue Cards:%2d"%(s.get_card_num('Red'), s.get_card_num('Blue')))
            s.stdscr.addstr(2, 70, "Red Pool:%2d                   Blue Pool:%2d"%(len(red.pool), len(blue.pool)))
        else:
            s.stdscr.addstr(1, 70, "Red Cards:%2d    turn: Blue    Blue Cards:%2d"%(s.get_card_num('Red'), s.get_card_num('Blue')))
            s.stdscr.addstr(2, 70, "Red Pool:%2d                   Blue Pool:%2d"%(len(red.pool), len(blue.pool)))

        s.stdscr.attroff(curses.A_BOLD)
        
        for i in range(5):
            if red.card[i].name:
                s.draw_card(red.card[i], i, -1, refresh=False, Type="Red")

        for i in range(5):
            if blue.card[i].name:
                s.draw_card(blue.card[i], i, -1, refresh=False, Type="Blue")
        
        for i in range(3):
            for j in range(3):
                h = s.board[i][j]
                if h.name:
                    s.draw_card(h, i, j, refresh=False);

        s.stdscr.refresh()
        s.stdscr.getch()

    def draw_card(s, h, x, y, color_skill=[], hightlight_dim=False, refresh=True, Type="Grid"):
        if Type == "Grid":
            posx, posy = 10 + 10 * x, 63 + 30 * y
        elif Type == "Red":
            posx, posy = 4 + x * 7, 15
        else:
            posx, posy = 4 + x * 7, 175

        s.stdscr.attron(curses.color_pair(3))
        for i in range(5):
            s.stdscr.addstr(posx+i-2, posy-5, " "*23);
        if h.name == "":
            return

        s.stdscr.attron(curses.A_BOLD)
        if h.owner == "Red":
            s.stdscr.attron(curses.color_pair(1))
        else:
            s.stdscr.attron(curses.color_pair(2))
        s.stdscr.addstr(posx-2, posy-5, h.name);
        s.stdscr.addstr(posx-1, posy-5, "品质: %d"%h.quality);
        s.stdscr.addstr(posx, posy-5, "阵营: %s"%h.camp);
        s.stdscr.addstr(posx+1, posy-5, "物种: %s"%h.sstr(h.species));
        s.stdscr.addstr(posx+2, posy-5, "技能: %s"%h.sstr(h.skill));
        if hightlight_dim:
            s.stdscr.attron(curses.color_pair(4))
        s.stdscr.addstr(posx-1, posy+9, "%d"%h.dimentions[0]);
        s.stdscr.addstr(posx-1, posy+13, "%d"%h.dimentions[1]);
        s.stdscr.addstr(posx-2, posy+11, "%d"%h.dimentions[2]);
        s.stdscr.addstr(posx, posy+11, "%d"%h.dimentions[3]);
        if hightlight_dim:
            s.stdscr.attroff(curses.color_pair(4))
        if color_skill:
            s.stdscr.attron(curses.color_pair(4))
            skills = h.sstr(h.skill)
            for skill in color_skill:
                index = skills.find(skill)
                if index >= 0:
                    for i in range(index):
                        if skills[i] in "1234-":
                            index += 2
                    s.stdscr.addstr(posx+2, posy+1+index, skill)
        s.stdscr.attroff(curses.A_BOLD)
        if refresh == True:
            s.stdscr.refresh()
            s.stdscr.getch()

if __name__ == "__main__":
    try:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED);
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_WHITE, -1)

        red = Player()
        blue = Player()
        bm = BattleManager()
        bm.draw_board(red, blue)


    except Exception as e:
        print(e)
    finally:
        curses.endwin()

