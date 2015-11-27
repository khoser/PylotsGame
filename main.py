# coding: utf-8

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color #, Canvas
from PylotsGame_class import PylotMap_class

class PG(Widget):
#    def __init__(self, d=10, *args, **kwargs):
#        Widget.__init__(self, *args, **kwargs)
#        self.d = d

    def fill(self,size,colortop,colorbottom,fieldSize):
        self.PM = PylotMap_class(size,colortop,colorbottom)
        self.fieldSize = fieldSize
        self.squareSize = fieldSize / size - 1
        self.redraw()

    def redraw(self):
        with self.canvas:
            Color(1,1,1)
            Rectangle(pos=(0, 0), size=(self.fieldSize,self.fieldSize))
            for i in self.PM.matr:
                for j in i:
                    Color(*j.color)
                    Rectangle(pos=(j.xplace * (self.squareSize + 1), j.yplace * (self.squareSize + 1)), size=(self.squareSize,self.squareSize))

    def findxplace(self, x):
        for i in range(self.PM.size):
            if self.PM.matr[i][i].xplace * (self.squareSize + 1) < x < self.PM.matr[i][i].xplace * (self.squareSize + 1) + self.squareSize:
                return self.PM.matr[i][i].xplace
        return -1


    def findyplace(self, y):
        for i in range(self.PM.size):
            if self.PM.matr[i][i].yplace * (self.squareSize + 1) < y < self.PM.matr[i][i].yplace * (self.squareSize + 1) + self.squareSize:
                return self.PM.matr[i][i].yplace
        return -1


    def on_touch_up(self, touch):
        xplace = self.findxplace(touch.y)
        yplace = self.findyplace(touch.x)
        if (xplace >= 0) and (yplace >=0):
            self.PM.invert(xplace,yplace)
        self.redraw()
        if self.PM.congratulation():
            self.makesometext()

    def makesometext(self):
        print("You won!")


class PylotsGameApp(App):
    def build(self):
        fieldSize = 300
        mwiget = AnchorLayout(anchor_x='center', anchor_y='top')
        menu = AnchorLayout(anchor_x='left', anchor_y='top')
        gm = AnchorLayout(anchor_x='center', anchor_y='center')
        colortop = (random(), random(), random())
        colorbottom = (random(), random(), random())
        game = PG()
        game.fill(4,colortop,colorbottom,fieldSize)
        gm.add_widget(game)

        btn = Button(text='New')
        menu.add_widget(btn)

        mwiget.add_widget(menu)
        mwiget.add_widget(gm)



        #mwiget = Widget()
        #mwiget.height
        #mwiget.canvas = Canvas(size = (300, 300), pos = (50, 50) )

        #n1 = PG(200)
        #n2 = PG(100)
        #mwiget.add_widget(n1)
        #mwiget.add_widget(n2)
        return mwiget


if __name__ == '__main__':
    PylotsGameApp().run()
