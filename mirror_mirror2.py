from graphics import *

def main():

    win = GraphWin('Basic Python Graphics', 1400, 1200) # give title and dimensions
    win.setBackground("black")
    myImage = Image(Point(700,150), "hat2.gif")
    myImage.draw(win)

    #print("lemons are nice")
    #win.yUp() # make right side up coordinates!

    ## BIG HEAD
    head = Circle(Point(700,400), 160) # set center and radius
    head.setFill("white")
    head.draw(win)

    ## EYES, NOSE AND MOUTH
    eye3a = Circle(Point(650, 300), 30)
    eye3a.setFill('lightblue')
    eye3a.draw(win)

    # Left Pupil
    eye3b = Circle(Point(650, 300), 8)
    eye3b.setFill('black')
    eye3b.draw(win)

    # Right Eyeball
    eye4a = Circle(Point(750, 300), 30)
    eye4a.setFill('lightblue')
    eye4a.draw(win)

    # Right Pupil
    eye4b = Circle(Point(750, 300), 8)
    eye4b.setFill('black')
    eye4b.draw(win)


    # Nose
    #nose1 = Oval(Point(650,350), Point(750,450)) # set center and radius
    #nose1.setFill("darkblue")
    #nose1.draw(win)

    nose2 = Polygon(Point(690,350), Point(690,400), Point(760,440), Point(710,350))
    nose2.setFill("darkblue")
    nose2.draw(win)

    mouth2 = Polygon(Point(600,480), Point(600,490), Point(800,490), Point(800,480))
    mouth2.setFill("red")
    mouth2.draw(win)

    mouth2s1 = Polygon(Point(800,480), Point(800,480), Point(810,480), Point(810,460))
    mouth2s1.setFill("red")
    mouth2s1.draw(win)

    mouth2s1 = Polygon(Point(600,480), Point(600,480), Point(590,480), Point(590,460))
    mouth2s1.setFill("red")
    mouth2s1.draw(win)


    # BIG TEXT AT BOTTOM
    message = Text(Point(win.getWidth()/2, 650), 'Mirror Mirror on the Wall.')
    message.draw(win)
    message.setTextColor("white")
    message.setSize(36)

    win.mainloop()

    win.getMouse()
    win.close()


    # Import
    #window = GraphWin("gameWindow", 800, 600)



main()
