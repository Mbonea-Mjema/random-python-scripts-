import bs4
class Point2D():
    def __init__(self, strcoord='0.0,0.0'):
        self.x, self.y = map(float, strcoord.split(','))
        self.name='ok'
    def printxy(self):
        print('x coord:',self.x)
        print('y coord:',self.y)
