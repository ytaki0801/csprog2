from abc import ABCMeta, abstractmethod

class Number(metaclass=ABCMeta):
  def __init__(self, v): self._value = v
  def __str__(self): return str(self._value) + ': ' + self._type
  def getType(self): return self._type
  @abstractmethod
  def add(n): pass

class Integer(Number):
  def __init__(self, v):
    super().__init__(v)
    self._type = '整数'
  def inc(self): self._value += 1
  def add(self, n):
    if isinstance(n, Integer): self._value += n._value
    else: print('型が異なります')

class Float(Number):
  def __init__(self, v):
    super().__init__(v)
    self._type = '浮動小数点数'
  def roundUp(self): return int(self._value) + 1
  def add(self, n):
    if isinstance(n, Float): self._value += n._value
    else: print('型が異なります')

i1, i2 = Integer(30), Integer(50); print(i1, i2)
f1, f2 = Float(5.7),  Float(2.4);  print(f1, f2)
i1.inc(); print(i1)
print(f1.roundUp())
i1.add(i2); print(i1)
i1.add(f1)
f1.add(f2); print(f1)
f1.add(i2)
#n = Number(10)
