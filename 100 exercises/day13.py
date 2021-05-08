'''
Question 47
Question
Define a class named Circle which can be constructed by a radius. The Circle class
has a method which can compute the area.
'''

class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        print( 3.14 * self.r * self.r)

aCircle = Circle(10)
# aCircle.area()

'''
Question 48
Question
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
'''

class Rectangle():
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print( self.l * self.w)

aRectangle = Rectangle(5, 4)
# aRectangle.area()

'''
Question 49
Question
Define a class named Shape and its subclass Square. The Square class has an init function 
which takes a length as argument. Both classes have a area function which can print the 
area of the shape where Shape's area is 0 by default.
'''
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

    def color(self, c):
        self.c = c

    def get_color(self):
        print (self.c)


class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.l = l

    def area(self):
        print( self.l ** 2)

aSquare = Square(5)
aSquare.area()
aSquare.color('red')
aSquare.get_color()

'''

Question 50
Question
Please raise a RuntimeError exception.
'''

raise RuntimeError('There is something wrong')

