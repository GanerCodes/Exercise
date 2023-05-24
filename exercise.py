from time import sleep
from random import choice
from subprocess import Popen

while True:
    sleep(30 * 60)
    print(f"{choice(range(10,15))}x {choice(('pushup', 'situp', 'lunge'))}s")
    Popen(["mpv", "--volume=50", "./sfx.mp3"])