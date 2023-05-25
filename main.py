import math
import turtle
from collections import deque

stack = deque()


def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = ' F+[[X]-X]-F[-FX]+X'  # Rule 1
    elif ch == 'F':
        newstr = 'FF'
    else:
        newstr = ch  # no rules apply so keep the character

    return newstr


def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        # if cmd == 'X':
         #   aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.left(angle)
        elif cmd == '-':
            aTurtle.right(angle)
        elif cmd == '[':
            stack.append((aTurtle.pos(), aTurtle.heading()))
        elif cmd == ']':
            aTurtle.up()
            coords = stack.pop()
            aTurtle.setpos(coords[0])
            aTurtle.setheading(coords[1])
            aTurtle.down()


def main():
    inst = createLSystem(6, "X")  # create the string
    print(inst)
    t = turtle.Turtle(shape="turtle")  # create the turtle
    wn = turtle.Screen()

    t.up()

    t.setpos(0, 0)
    t.left(25)
    t.down()
    t.speed(40)
    drawLsystem(t, inst, 25, 4)  # draw the picture
    # angle 60, segment length 5
    wn.exitonclick()


main()
