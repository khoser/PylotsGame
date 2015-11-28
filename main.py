# coding: utf-8

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from kivy.graphics import Rectangle, Color #, Canvas
from PylotsGame_class import PylotMap_class

class PG(Widget):

    count = NumericProperty(0)
    fieldSize = NumericProperty(300)

#    def __init__(self, d=10, *args, **kwargs):
#        Widget.__init__(self, *args, **kwargs)
#        self.d = d

    def fill(self,size,colortop,colorbottom,fieldSize):
        self.PM = PylotMap_class(size,colortop,colorbottom)
        self.fieldSize = fieldSize + 1
        self.squareSize = fieldSize / size - 1
        self.x_clarif = 0
        self.y_clarif = 0


    def newgame(self):
        self.PM.new()
        self.count = self.PM.count

        self.redraw()


    def redraw(self):
        with self.canvas:
            Color(1,1,1)
            Rectangle(pos=(-self.x_clarif, -self.y_clarif), size=(self.fieldSize,self.fieldSize))
            for i in self.PM.matr:
                for j in i:
                    Color(*j.color)
                    Rectangle(pos=(1+j.xplace * (self.squareSize + 1)-self.x_clarif, 1+j.yplace * (self.squareSize + 1)-self.y_clarif), size=(self.squareSize,self.squareSize))

    def findxplace(self, x):
        for i in range(self.PM.size):
            if 1 + self.PM.matr[i][i].xplace * (self.squareSize + 1) - self.x_clarif < x < 1 + self.PM.matr[i][i].xplace * (self.squareSize + 1) + self.squareSize - self.x_clarif:
                return self.PM.matr[i][i].xplace
        return -1


    def findyplace(self, y):
        for i in range(self.PM.size):
            if 1 + self.PM.matr[i][i].yplace * (self.squareSize + 1) - self.y_clarif < y < 1 + self.PM.matr[i][i].yplace * (self.squareSize + 1) + self.squareSize - self.y_clarif:
                return self.PM.matr[i][i].yplace
        return -1


    def on_touch_up(self, touch):
        xplace = self.findxplace(touch.y)
        yplace = self.findyplace(touch.x)
        if (xplace >= 0) and (yplace >=0):
            self.PM.invert(xplace,yplace)
            self.count = self.PM.count
        self.redraw()
        if self.PM.congratulation():
            self.makesometext()

    def makesometext(self):
        print("You won!")


    def onbuttonpress(self):

        colortop = (random(), random(), random())
        colorbottom = (random(), random(), random())

        fieldSize = 300
        fieldnum = 4

        self.fill(fieldnum,colortop,colorbottom,fieldSize)
        self.newgame()


class GameDesk(Widget):
    pg = ObjectProperty(None)

    def onbuttonpress(self):
        self.pg.onbuttonpress()


class PylotsGameApp(App):
    def build(self):

        game = GameDesk()

        game.onbuttonpress()


        return game


if __name__ == '__main__':
    PylotsGameApp().run()
