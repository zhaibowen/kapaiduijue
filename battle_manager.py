#coding=utf-8
import curses
import os
import random
import sys
import time
from hero import Hero
from player import Player

class BattleManager:
    def __init__(s, draw=True):
        s.width = 3
        s.height = 3
        s.turn = random.randint(0, 1)
        s.board = [[Hero() for j in range(s.height)] for i in range(s.width)]
        s.valid = s.width * s.height
        s.total_grid = s.width * s.height
        s.cur_posx = -1
        s.cur_posy = -1
        s.draw = draw
    
    def has_place(s):
        return s.valid > 0

    def turn_over(s):
        s.turn ^= 1

    def inference(s, red, blue):
        pass

    def draw_board(s, stdscr, red, blue):
        if s.draw == False:
            return
        #rows, cols = stdscr.getmaxyx()
        stdscr.attron(curses.color_pair(3))
        #for i in range(rows):
        #    stdscr.addstr(i, 0, " "*(cols-1))
        stdscr.clear()
        for i in range(30):
            stdscr.addstr(5 + i, 50, "|                              |                              |                              |")
        for i in range(4):
            stdscr.addstr(5 + i * 10, 50, "----------------------------------------------------------------------------------------------")
        for i in range(5):
            stdscr.addstr(7 + i * 7, 5, "-----------------------------")
            stdscr.addstr(7 + i * 7, 165, "-----------------------------")

        if s.turn == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(1, 70, "turn: Red")
        else:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(1, 70, "turn: Blue")
        
        stdscr.attron(curses.color_pair(1))
        for i in range(5):
            if red.card[i].name:
                s.draw_card(stdscr, red.card[i], 4 + i * 7, 15)

        stdscr.attron(curses.color_pair(2))
        for i in range(5):
            if blue.card[i].name:
                s.draw_card(stdscr, blue.card[i], 4 + i * 7, 175)
        
        for i in range(3):
            for j in range(3):
                h = s.board[i][j]
                if h.name:
                    if h.owner == "Red":
                        stdscr.attron(curses.color_pair(1))
                    else:
                        stdscr.attron(curses.color_pair(2))
                    s.draw_card(stdscr, h, 5 + 10 * i + 5, 50 + 30 * j + 13);

        stdscr.refresh()
        time.sleep(1e0)

    def draw_card(s, stdscr, h, posx, posy):
        stdscr.addstr(posx-2, posy-5, h.name);
        stdscr.addstr(posx-1, posy-5, "品质: %d"%h.quality);
        stdscr.addstr(posx, posy-5, "阵营: %s"%h.camp);
        stdscr.addstr(posx+1, posy-5, "物种: %s"%h.sstr(h.species));
        stdscr.addstr(posx+2, posy-5, "技能: %s"%h.sstr(h.skill));
        stdscr.addstr(posx-1, posy+9, "%d"%h.dimentions[0]);
        stdscr.addstr(posx-1, posy+13, "%d"%h.dimentions[1]);
        stdscr.addstr(posx-2, posy+11, "%d"%h.dimentions[2]);
        stdscr.addstr(posx, posy+11, "%d"%h.dimentions[3]);

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

