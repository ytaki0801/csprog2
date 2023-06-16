class Car:
  def __init__(self, n=0, g=0.0):
    self.__num = n
    self.__gas = g
  def __str__(self):
    return '(num)' + str(self.__num) + ' (gas)' + str(self.__gas)
  def setCar(self, n, g):
    self.__num = n
    self.__gas = g
  def compareGas(self, a):
    if   self.__gas > a.__gas: return 1
    elif self.__gas < a.__gas: return -1
    else: return 0

car1, car2 = Car(1234, 25.5), Car(6789, 40)
print(car1, car2, sep=', ')
car2 = car1
print(car1, car2, sep=', ')
car1.setCar(4567, 10.5)
print(car1, car2, sep=', ')
car2 = Car(6789, 40)
print(car1, car2, sep=', ')
print(car1.compareGas(car2), car2.compareGas(car1))
