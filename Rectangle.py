class Rectangle:

  def __init__(self, x, y, h, w):
    '''Takes x, y coordinates, as well as a width and height, and saves them as instance variables'''
    self.x = max(0, x)
    self.y = max(0, y)
    self.height = max(0, h)
    self.width = max(0, w)

def __str__(self):
  '''returns a string containing the x, y, width, and height of the rectangle'''

  s="(x: {}, y: {}) width: {}, height: {}"

  return s.format(self.x, self.y, self.width, self.height)