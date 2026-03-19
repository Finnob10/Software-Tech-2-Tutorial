from tkinter import *
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")

        self.width = 400
        self.height = 400
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Koch Snowflake",
               command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        order = int(self.order.get())

        cx, cy = self.width / 2, self.height / 2
        r = 150

        p1 = [cx + r * math.cos(-math.pi / 2),
              cy + r * math.sin(-math.pi / 2)]
        p2 = [cx + r * math.cos(-math.pi / 2 + 2 * math.pi / 3),
              cy + r * math.sin(-math.pi / 2 + 2 * math.pi / 3)]
        p3 = [cx + r * math.cos(-math.pi / 2 + 4 * math.pi / 3),
              cy + r * math.sin(-math.pi / 2 + 4 * math.pi / 3)]

        self.kochCurve(order, p1, p2)
        self.kochCurve(order, p2, p3)
        self.kochCurve(order, p3, p1)

    def kochCurve(self, order, p1, p2):
        if order == 0:
            self.drawLine(p1, p2)
        else:
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            a = [p1[0] + dx / 3,     p1[1] + dy / 3]
            b = [p1[0] + 2 * dx / 3, p1[1] + 2 * dy / 3] 
            m = [a[0] + (b[0] - a[0]) * 0.5 + (b[1] - a[1]) * math.sqrt(3) / 2,
            a[1] + (b[1] - a[1]) * 0.5 - (b[0] - a[0]) * math.sqrt(3) / 2]

            self.kochCurve(order - 1, p1, a)
            self.kochCurve(order - 1, a,  m)
            self.kochCurve(order - 1, m,  b)
            self.kochCurve(order - 1, b,  p2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line")

KochSnowflake()