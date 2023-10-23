class Car:
  def __init__(self, *props):
    if props:
      self.prop = props
    else:
      self.prop = '', 0
  @property
  def prop(self):
    return self.__name + str(self.__num).zfill(4)
  @prop.setter
  def prop(self, props):
    name, num = props[0], props[1]
    if isinstance(name, str):
      self.__name = name
    else:
      print('名前が文字列ではありません')
    if isinstance(num, int) and num < 10000 and num >= 0:
      self.__num = props[1]
    else:
      print('ナンバーの値が不正です')

car1 = Car(); print(car1.prop)
car2 = Car('カローラ', 567); print(car2.prop)
car1.prop = 678, 'プリウス'; print(car1.prop)
car1.prop = 'プリウス', 678; print(car1.prop)
