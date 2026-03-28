from graphics import *


def draw3Circles(n1, n2, n3):
    win = GraphWin("3 Circles", 800, 600)

    radii = sorted([n1, n2, n3], reverse=True)
    a, b, c = radii[0], radii[1], radii[2]

    center = Point(400, 300)

    circle1 = Circle(center, a)
    circle1.setOutline("purple")
    circle1.setFill("yellow")

    circle2 = Circle(center, b)
    circle2.setOutline("red")
    circle2.setFill("blue")

    circle3 = Circle(center, c)
    circle3.setOutline("orange")
    circle3.setFill("green")

    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)

    win.getMouse()
    win.close()


def PrintNumsWithSum(n, m):
    for i in range(m, n):
        number = i
        count = 0

        while number > 0:
            count += number % 10
            number //= 10

        if count == m:
            print(i)


def DrawFace(eye1, eye2, mouth, noise):
    win = GraphWin("Face", 600, 600)

    head = Circle(Point(300, 300), 200)
    head.setFill("yellow")
    head.draw(win)

    leftEye = Circle(Point(250, 200), eye1)
    rightEye = Circle(Point(350, 200), eye2)
    leftEye.setFill("green")
    rightEye.setFill("green")
    leftEye.draw(win)
    rightEye.draw(win)

    noise1 = Rectangle(Point(290, 250), Point(310, 250 + noise))
    noise1.setFill("red")
    noise1.draw(win)

    pt1 = Point(250, 360)
    pt2 = Point(250 + mouth, 360)
    mouth1 = Line(pt1, pt2)
    mouth1.setWidth(10)
    mouth1.setFill("pink")
    mouth1.draw(win)

    win.getMouse()
    win.close()


# דוגמאות להרצה:
draw3Circles(180, 130, 90)
PrintNumsWithSum(100, 5)
DrawFace(20, 20, 100, 50)