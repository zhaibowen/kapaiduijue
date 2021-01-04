#coding=utf-8
import curses
import os
import random
import sys
import traceback
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

        for epoch in range(10000):
            if epoch % 1000 == 0:
                print(epoch)
            red = Player('Red')
            blue = Player('Blue')
            #print(epoch)
            #print(red.card[0].name)
            #print(blue.card[0].name)
            bm = BattleManager(stdscr=False, save_record=1)
            #bm = BattleManager(stdscr=stdscr, save_record=1)
            while bm.has_place(red, blue):
                bm.draw_board(red, blue)
                if bm.turn == 0:
                    hero, card_pos, posx, posy = red.move(bm, blue)
                    bm.inference(red, blue, hero, posx, posy, card_pos=card_pos)
                else:
                    hero, card_pos, posx, posy = blue.move(bm, red)
                    bm.inference(blue, red, hero, posx, posy, card_pos=card_pos)
                bm.draw_board(red, blue)
                bm.turn_over()

            bm.show_winner()

    except Exception as e:
        traceback.print_exc()
    finally:
        curses.endwin()

if __name__ == "__main__":
    main()

