import sys

sys.path.append("./mod")

import socket
import time
import threading
import curses

def main(stdscr):
    curses.noecho()
    def sender():
        while 1:
            stdscr.move(0, 0)
            c = ''
            data = ""
            while c != curses.KEY_ENTER:
                c = stdscr.getch()
                if c == curses.KEY_ENTER:
                    break
                elif c == curses.KEY_BACKSPACE:
                    data = data[:-1]
                    c = ""
                else:
                    c = chr(c)
                data += c
            with open("out.txt", 'w') as outFile:
                stdscr.addstr(3, 3, "thisaiafe")
                outFile.write(data)
    def ui():
        cy = 0
        out = ""
        rc = ""
        while 1:
            with open("out.txt", 'r') as outFile:
                out = outFile.read()
            stdscr.addstr(2, 0, "sent %s" % out)
            stdscr.addstr(5, 0, str(cy))
            time.sleep(.2)
            stdscr.move(0, 0)
            with open("out.txt", 'w') as outFile:
                outFile.write("")
            stdscr.refresh()
            cy += 1
    threading.Thread(None, sender, None, (), {}).start()
    threading.Thread(None, ui, None, (), {}).start()

curses.wrapper(main)
