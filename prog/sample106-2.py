class Fraction:
  n = 0
  d = 1
  def setValues(self,x,y):
    self.n = x
    self.d = y
  def printValues(self):
    print(self.n, "/", self.d)
  def plus(self, c):
    x = Fraction()
    x.setValues(self.n * c.d + self.d * c.n, self.d * c.d)
    return(x)

# >>> a = Fraction()
# >>> a.setValues(1,2)
# >>> b = Fraction()
# >>> b.setValues(1,3)
# >>> c = a.plus(b)
# >>> c.printValues()
# 5 / 6
