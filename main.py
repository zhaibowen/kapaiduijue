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

        red = Player('Red')
        blue = Player('Blue')
        bm = BattleManager(draw=True)
        while bm.has_place():
            bm.draw_board(stdscr, red, blue)
            if bm.turn == 0:
                red.move(bm)
            else:
                blue.move(bm)
            bm.draw_board(stdscr, red, blue)
            bm.inference(red, blue)
            bm.draw_board(stdscr, red, blue)
            bm.turn_over()

    except Exception as e:
        print(e)
    finally:
        curses.endwin()

if __name__ == "__main__":
    main()

