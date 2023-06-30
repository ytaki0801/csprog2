class Car:
  def __init__(self, n=0, g=0.0):
    self._num, self.__gas = n, g
  def __str__(self):
    print('- Carの特殊メソッド__str__ -')
    return '(num)' + str(self._num) + ' (gas)' + str(self.__gas)
  def getNum(self):
    print('- CarのメソッドgetNum -')
    return self._num
  def setNum(self, n):
    print('- CarのメソッドsetNum -')
    if n > 0: self._num = n; print('done.')
    else: print('Out of range.')
  def getGas(self):
    print('- CarのメソッドgetGas -')
    return self.__gas
  def setGas(self, g):
    print('- CarのメソッドsetGas -')
    if g > 0: self.__gas = g; print('done.')
    else: print('Out of range.')

class RacingCar(Car):
  def __str__(self):
    print('- RacingCarの特殊メソッド__str__ -')
    r = '(num)' + str(self._num)
    #r += ' (gas)' + str(self.__gas)
    r += ' (course)' + str(self.__course)
    return r
  def getCource(self):
    print('- RacingCarのメソッドgetCource -')
    return self.__cource
  def setCource(self, c):
    print('- RacingCarのメソッドsetCource -')
    self.__course = c; print('done.')

c1, rc1 = Car(), RacingCar()

print('===== ここからc1 =====')
c1.setGas(500)
c1.setGas(-500)
c1.setNum(5678)
print(c1)

print('===== ここからrc1 =====')
rc1.setCource(7)
rc1.setNum(1234)
rc1.setGas(-200)
rc1.setGas(300);
print(rc1)