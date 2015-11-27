# coding: utf-8

from random import random


class PylotSquare_class():
  def __init__(self, xplace, yplace, color):
    self.xplace = xplace
    self.yplace = yplace
    self.color = color

  def print_info(self):
    return "_{}_{}".format(self.xplace, self.yplace)


class PylotMap_class():

  def __init__(self, size, colortop, colorbottom):
    #self.count = 0
    self.size = int(size)
    self.colorbottom = colorbottom
    self.colortop = colortop
    #self.matr = [[PylotSquare_class(i, j, getcolor(random(), colortop, colorbottom)) for i in xrange(self.size)] for j in xrange(self.size)]
    self.new()

  def new(self):
    def getcolor(tmp1, colortop, colorbottom):
      if tmp1 < 0.5:
        clr_rnd = colorbottom
      else:
        clr_rnd = colortop
      return clr_rnd
    self.count = 0
    self.matr = [[PylotSquare_class(i, j, getcolor(random(), self.colortop, self.colorbottom)) for i in xrange(self.size)] for j in xrange(self.size)]

  def showmap(self):
    for i in self.matr:
      str = ""
      for j in i:
        str = str + j.color + "\t"
      print str

  def invertself(self, xplace, yplace):
    if self.matr[xplace][yplace].color == self.colorbottom:
      self.matr[xplace][yplace].color = self.colortop
    else:
      self.matr[xplace][yplace].color = self.colorbottom

  def invertrow(self, xplace, yplace):
    for i in xrange(self.size):
      if i == xplace:
        continue
      self.invertself(i, yplace)

  def invertcol(self, xplace, yplace):
    for i in xrange(self.size):
      if i == yplace:
        continue
      self.invertself(xplace, i)

  def invert(self, xplace, yplace):
    self.invertcol(xplace, yplace)
    self.invertrow(xplace, yplace)
    self.invertself(xplace, yplace)
    self.count += 1

  def congratulation(self):
    k = self.matr[0][0]
    for i in self.matr:
      for j in i:
        if j.color != k.color:
          return False
        k = j
    return True
