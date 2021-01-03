#coding=utf-8
import curses
import os
import random
import sys
import time
from player import Player
from battle_manager import BattleManager

def main():
    try:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED);
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_WHITE, -1)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)

        red = Player('Red')
        blue = Player('Blue')
        #bm = BattleManager(stdscr=False)
        bm = BattleManager(stdscr=stdscr)
        while bm.has_place(red, blue):
            bm.draw_board(red, blue)
            if bm.turn == 0:
                hero, posx, posy = red.move(bm)
            else:
                hero, posx, posy = blue.move(bm)
            bm.preprocess_board()
            bm.draw_board(red, blue)
            if bm.turn == 0:
                bm.inference(red, blue, hero, posx, posy)
            else:
                bm.inference(blue, red, hero, posx, posy)
            bm.draw_board(red, blue)
            bm.turn_over()

        bm.show_winner()

    except Exception as e:
        print(e)
    finally:
        curses.endwin()

if __name__ == "__main__":
    main()

