from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Rectangle, Color #, Canvas


class PG(Widget):
#    def __init__(self, d=10, *args, **kwargs):
#        Widget.__init__(self, *args, **kwargs)
#        self.d = d

    def fill(self):
        pass

    def on_touch_up(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            #Rectangle(pos=(self.center_x - self.d/2, self.center_y - self.d/2), size=(self.d,self.d))
            #Rectangle(pos=(0, 0), size=(self.d,self.d))
            #Rectangle(pos=(self.width-self.d/2, self.height-self.d/2), size=(self.d,self.d))
      

class PylotsGameApp(App):
    def build(self):
        mwiget = AnchorLayout(size=(300, 300))
        #btn = Button(text='Hello World')
        #layout.add_widget(btn)

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
