import curses
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()

    win = curses.newwin(1, 20, 10, 10)

    for i in range(100):
        win.clear()

        win.addstr(f"Count: {i}")
        win.refresh()
        time.sleep(.1)
    stdscr.getch()
    

if __name__ == "__main__":
    curses.wrapper(main)