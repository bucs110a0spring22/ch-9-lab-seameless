from Rectangle import Rectangle

class Surface:

  def __init__(self, file, x, y, h, w):
    '''Takes the filename string as a parameter and saves it to the self.image instance variable'''

    self.image = file

    self.rect = Rectangle(x, y, h, w)


  def getRect(self):
    '''returns the rectangle object'''

    return self.rect