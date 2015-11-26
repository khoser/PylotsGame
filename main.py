from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class PG(Widget):
  d = 10;
  def __init__(self, d=10, *args, **kwargs):
    Widget.__init__(self, *args, **kwargs)
    self.d = d

  def on_touch_down(self, touch):
    color = (random(), random(), random())
    with self.canvas:
      Color(*color)
      Rectangle(pos=(self.center_x - 100, self.center_y - 100), size=(self.d,self.d))
      

class PylotsGameApp(App):
  def build(self):
    return PG(150)


if __name__ == '__main__':
  PylotsGameApp().run()
