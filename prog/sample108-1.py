class Date:
  def __init__(self, a=(1970, 1, 1)):
    if isinstance(a, Date):
      self.__year, self.__month, self.__day = a.__year, a.__month, a.__day
    else:
      self.__year, self.__month, self.__day = a
  def setYMD(self, a):
    self.__year, self.__month, self.__day = a
  def __str__(self):
    r = str(self.__year).zfill(4)
    r += '/' + str(self.__month).zfill(2)
    r += '/' + str(self.__day).zfill(2)
    return r

class Car:
  def __init__(self, n=0, g=0.0):
    self.__num, self.__gas, self.__buy = n, g, Date()
  def __str__(self):
    r = '(num)' + str(self.__num) + ' (gas)' + str(self.__gas) + '\n'
    r += self.__buy.__str__()
    return r
  def setCar(self, n, g):
    self.__num, self.__gas = n, g
  def setBuy(self, d):
    self.__buy = d
  def getBuy(self):
    return self.__buy
  def getBuyCopy(self):
    return Date(self.__buy)

d1 = Date(); print(d1)
d1 = Date((2015, 5, 15)); print(d1)
print()

c1 = Car(1234, 50); print(c1)
d1 = c1.getBuy();
d1.setYMD((2013, 7, 8)); print(d1)
d1 = c1.getBuyCopy();
d1.setYMD((2015, 4, 24)); print(d1)
