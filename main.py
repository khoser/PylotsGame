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
    fieldSize = NumericProperty(0)

    def fill(self,size,colortop,colorbottom,fieldSize):
        self.PM = PylotMap_class(size,colortop,colorbottom)
        self.fieldSize = fieldSize
        self.squareSize = (self.fieldSize - size -1) * 1.0 / size


    def newgame(self):
        self.PM.new()
        self.count = self.PM.count

        self.redraw()


    def redraw(self):
        self.canvas.clear()
        with self.canvas:

            Color(1,1,1)
            Rectangle(pos=(0, 0), size=(self.fieldSize,self.fieldSize))
            for i in self.PM.matr:
                for j in i:
                    Color(*j.color)
                    Rectangle(pos=(1+j.xplace * (self.squareSize + 1), 1+j.yplace * (self.squareSize + 1)), size=(self.squareSize,self.squareSize))

    def findxplace(self, x):
        for i in range(self.PM.size):
            if 1 + self.PM.matr[i][i].xplace * (self.squareSize + 1) < x < 1 + self.PM.matr[i][i].xplace * (self.squareSize + 1) + self.squareSize:
                return self.PM.matr[i][i].xplace
        return -1


    def findyplace(self, y):
        for i in range(self.PM.size):
            if 1 + self.PM.matr[i][i].yplace * (self.squareSize + 1) < y < 1 + self.PM.matr[i][i].yplace * (self.squareSize + 1) + self.squareSize:
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
        self.lbl.text = "You won! {0}".format(self.count)


    def onbuttonpress(self,lbl,txt):
        self.lbl = lbl

        colortop = (random(), random(), random())
        colorbottom = (random(), random(), random())

        fieldSize = self.parent.width

        self.fill(int(txt.text),colortop,colorbottom,fieldSize)
        self.newgame()


class GameDesk(Widget):

    pg = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(GameDesk, self).__init__(**kwargs)
        self.size_hint_x = 1.0

    def onbuttonpress(self):
        self.pg.onbuttonpress(self.ids.lbl, self.ids.txtinp)


class PylotsGameApp(App):
    def build(self):

        game = GameDesk()
        game.onbuttonpress()

        return game


if __name__ == '__main__':
    PylotsGameApp().run()
