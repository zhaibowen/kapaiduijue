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
        curses.echo()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED);
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_WHITE, -1)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)

        red_elo = 1000
        blue_elo = 1000
        red_knt = 0
        blue_knt = 0
        equal_knt = 0

        for epoch in range(10000):
            if epoch % 1000 == 0:
                print(epoch)
                print("red_elo:", red_elo)
                print("blue_elo:", blue_elo)
                print("red_knt:", red_knt)
                print("blue_knt:", blue_knt)
                print("equal_knt:", equal_knt)
            red = Player('Red', mode='random', select_card="random")
            blue = Player('Blue', mode='random', select_card="default")
            #red = Player('Red', mode='human', select_card="default", stdscr=stdscr)
            #blue = Player('Blue', mode='human', select_card="default", stdscr=stdscr)
            #print(epoch)
            #print(red.card[0].name)
            #print(blue.card[0].name)
            #bm = BattleManager(stdscr=False, save_record=1)
            bm = BattleManager(stdscr=stdscr, save_record=2)
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
            red_elo, blue_elo, red_knt, blue_knt, equal_knt = bm.compute_elo(red_elo, blue_elo, red_knt, blue_knt, equal_knt)

    except Exception as e:
        traceback.print_exc()
    finally:
        curses.endwin()

if __name__ == "__main__":
    main()

