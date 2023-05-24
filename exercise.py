from time import sleep
from random import choice
from subprocess import Popen

display, m = lambda x: f"{x//60:0<2}:{x%60:0<2}", ""
while True:
    for x in range(k := 30 * 60, 0, -1):
        print(display(x), '/', display(k), m)
        sleep(1)
    print("Excercise time",
        m := f"{choice(range(10, 15))}x {choice(('pushup', 'situp', 'lunge'))}s")
    Popen(["mpv", "--volume=50", "./sfx.mp3"])