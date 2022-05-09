from math import sqrt
class Point2D:
  __count=0
  def __init__(self, x, y):
    self.x=x
    self.y=y
    Point2D.__count+=1
    self.__count=Point2D.__count
  
  @property
  def count(self):
    return f"Це {self.__count}-й екземпляр класу Point2D" 
  
  def get_count():
    return F"Усього ініціалізовано {Point2D.__count} екземплярів класу Point2D"
  
  def distance(self, obj):
    return f"2D відстань між {self} {obj} => {sqrt(pow((self.x-obj.x),2)+pow((self.y-obj.y),2))}"

  def __str__(self):
    return f"Точка x={self.x} y={self.y}"

class Point3D(Point2D):
  def __init__(self, x,y,z):
    super().__init__(x,y)
    self.z=z
  def distance(self, obj):
    return f"3D відстань між {self} та {obj} => {sqrt(pow((self.x-obj.x),2)+pow((self.y-obj.y),2)+pow((self.z-obj.z),2))}"
  def __str__(self):
    return f"Точка x={self.x} y={self.y} z={self.z}"

p=Point2D(-10,20)
p1=Point2D(44,33)
p2=Point2D(0,89)
p3=Point2D(0,89)
print(p.distance(p1))
print(Point2D.get_count())
print(p,p.count)
print(p1,p1.count)
print("-------------")
c=Point3D(-10,0,11)
c1=Point3D(20,22,22)
print( c.distance(c1))
print(c, c1.count)
print( Point3D.get_count())
