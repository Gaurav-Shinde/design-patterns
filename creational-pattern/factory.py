from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def draw(self):
    pass

class Rectangle(Shape):
    # instance method, use self
  def draw(self):
    print("I am a rectangle")

class Square(Shape):
  def draw(self):
    print("I am a square")

class Triangle(Shape):
    def draw(self):
      print("I am a triangle")

class ShapeFactory():
  def create_shape(self,shape: str):
    if(shape == "Rectangle"):
      return Rectangle()
    if(shape == "Square"):
      return Square()
    if(shape == "Triangle"):
      return Triangle()

if __name__ == "__main__":
  factory: ShapeFactory = ShapeFactory()
  my_rectangle: Rectangle = factory.create_shape("Rectangle")
  my_rectangle.draw()
  my_triangle: Triangle = factory.create_shape("Triangle")
  my_triangle.draw()
    
