class ArithmeticMixin:
  @staticmethod
  def sum(a,b):
    return a+b

  @staticmethod
  def sub(a,b):
    return a-b
  
  @staticmethod
  def mul(a,b):
    return a*b

  @staticmethod
  def div(a,b):
    if b==0:
       raise ValueError("Не можна ділити на нуль!")
    return a/b

class Fraction(ArithmeticMixin):
  def __init__(self,num,den):
    self.num=num
    self.den=den

  @classmethod
  def str_fraction(cls, astring):
    if astring[1] != '/':
      raise ValueError("Невірний ввід даних!")
    if not astring[0].lstrip('-').isdigit() or not astring[2].lstrip('-').isdigit():
      raise ValueError("Помилка при вводі чисел!")
    if astring[2]=="0":
      raise ValueError("Не можна ділити на нуль!")
    astring=astring.split("/")
    
    num, den=int(astring[0]), int(astring[1])
    return cls(num, den)
  
  @property
  def num(self):
    return self.__num

  @num.setter
  def num(self, num):
    self.__num=num
    return self.__num

  @property
  def den(self):
    return self.__den

  @den.setter
  def den(self, den):
      if den==0:
        raise ValueError("Не можна ділити на нуль!")
      self.__den=den
      return self.__den

  def __add__(self, obj):
    return float(self.num/self.den)+float(obj.num/obj.den)

  def __sub__(self, obj):
    return float(self.num/self.den)-float(obj.num/obj.den)

  def __mul__(self, obj):
    return float(self.num/self.den)*float(obj.num/obj.den)

  def __truediv__(self, obj):
    return float(self.num/self.den)/float(obj.num/obj.den)

  def __str__(self):
    return f"{self.num} / {self.den}"
    



r=Fraction(44,40)
s=Fraction(10,10)
print("Вивід обєкту за допомогою методу __str___") 
print(r)
print(s)
print("Вивід статичних методів реалізованих у міксіні")
print("sum = ",s.sum(r,s))
print("sub = ",s.sub(r,s))
print("mul = ",r.mul(r,s))
print("div = ",r.div(r,s))
print("Вивід перевизначених методів __sub__ тощо")
print("sum = ",r+s)
print("sub = ", r-s)
print("mul = ",r*s)
print("div = ",r/s)
print("Вивід обєкту перевизначеного через classmethod")
astr=s.str_fraction("3/1")
print(astr)
print(s+astr)