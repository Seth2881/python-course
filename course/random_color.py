from sty import fg,bg
import random as whopper
import time as t
import sys

sys.stdout.write("\033[?25l")

def cprint(color,color_bg,prompt)->None :
    sys.stdout.write("\r" + " " * 30 + "\r")  # efface la ligne
    sys.stdout.write(bg(color_bg[0],color_bg[1],color_bg[2])+fg(color[0],color[1],color[2])+prompt+fg.rs+bg.rs)
    sys.stdout.flush()
    t.sleep(0.15)


def super_cool_ass_color()->list[int] :
    return whopper.randint(0,255),whopper.randint(0,255),whopper.randint(0,255)

for _ in range(100) :
    color = super_cool_ass_color()
    color_bg = super_cool_ass_color()
    cprint(color,color_bg,'hello World')
sys.stdout.write("\r" + " " * 30 + "\r")  # efface la ligne
print(fg.red+';^)'+fg.rs)