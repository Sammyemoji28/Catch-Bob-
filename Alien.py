
import pgzrun

WIDTH = 500
HEIGHT = 500
TITLE = "Catch the Aliens!!"

message = ""

#creating characters! yay

bob = Actor("alien")
bob.pos = (182,374)

def draw():
    print('hi')
    bob.draw()


pgzrun.go()