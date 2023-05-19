class Fraction:
  n = 0
  d = 1
  def __init__(self,x,y):
    self.n = x
    self.d = y
  def __str__(self):
    return str(self.n) + "/" + str(self.d)
  def __add__(self, c):
    x = Fraction(self.n * c.d + self.d * c.n, self.d * c.d)
    return(x)
  def __mul__(self, c):
    x = Fraction(self.n * c.d + self.d * c.n, self.d * c.d)
    return(x)

# >>> a = Fraction(1,2)
# >>> b = Fraction(1,3)
# >>> print(a,b)
# 1/2 1/3
# >>> print(a+b)
# 5/6
# >>> print(a*b)
# 1/6
