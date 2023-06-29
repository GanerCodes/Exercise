from os import path
from sys import argv
from time import sleep
from random import choice, gauss
from subprocess import Popen, DEVNULL
from datetime import date

para = (30, 12, 30)

days = lambda: (date.today() - date(2023, 6, 29)).days
dist = lambda x,t,s,m: s+(t-s)*x/(x+m)
amnt = lambda: (k:=dist(days(), *para))+0.2*k*gauss(0,1)
# https://www.desmos.com/calculator/2slbgxunlg

display, m = lambda x: f"{x//60:0>2}:{x%60:0>2}", ""
while True:
    for x in range(k := 30 * 60, 0, -1):
        print(display(x), '/', display(k), m)
        sleep(1)
    print("Excercise time",
        m := f"{amnt()}x {choice(('pushup', 'situp', 'lunge'))}s")
    Popen(["mpv", "--volume=50", path.join(path.dirname(argv[0]), "sfx.mp3")], stdout=DEVNULL, stderr=DEVNULL)
