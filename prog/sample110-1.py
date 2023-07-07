class Car:
  def __init__(self, n=0, g=0.0):
    print('- Carのコンストラクタ__init__ -')
    self.__num, self.__gas = n, g
  def __str__(self):
    print('- Carの特殊メソッド__str__ -')
    return '(num)' + str(self.__num) + ' (gas)' + str(self.__gas)

class RacingCar(Car):
  def __init__(self, n=0, g=0.0, c=0):
    print('- RacingCarのコンストラクタ__init__ -')
    super().__init__(n, g)
    self.__course = c
  def __str__(self):
    print('- RacingCarの特殊メソッド__str__ -')
    r = super().__str__()
    r += ' (course)' + str(self.__course)
    return r

cars = []

cars.append(RacingCar(1357, 45.0, 2))
cars.append(Car(4321, 25.0))
cars.append(RacingCar(9876, 30.5, 6))

for x in cars: print(x)