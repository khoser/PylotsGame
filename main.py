from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class PG(Widget):
  def __init__(self, d=10, *args, **kwargs):
    Widget.__init__(self, *args, **kwargs)
    self.d = d

  def on_touch_down(self, touch):
    color = (random(), random(), random())
    with self.canvas:
      Color(*color)
      Rectangle(pos=(self.center_x - self.d/2, self.center_y - self.d/2), size=(self.d,self.d))
      #Rectangle(pos=(self.width-self.d/2, self.height-self.d/2), size=(self.d,self.d))
      

class PylotsGameApp(App):
  def build(self):
    mwiget = Widget()
    #mwiget.height

    n1 = PG(200)
    n2 = PG(100)
    mwiget.add_widget(n1)
    mwiget.add_widget(n2)
    return mwiget


if __name__ == '__main__':
  PylotsGameApp().run()
