import curses

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(5, 10, f"* {height}x{width} *")
    stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)