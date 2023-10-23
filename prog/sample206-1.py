class Car:
  def __init__(self, *props):
    if props:
      self.setProp(*props)
    else:
      self.setProp('', 0)
  def getProp(self):
    return self.__name + str(self.__num).zfill(4)
  def setProp(self, *props):
    if isinstance(props[0], str):
      self.__name = props[0]
    else:
      print('名前が文字列ではありません')
    if isinstance(props[1], int) and props[1] < 10000 and props[1] >= 0:
      self.__num = props[1]
    else:
      print('ナンバーの値が不正です')

car1 = Car(); print(car1.getProp())
car2 = Car('カローラ', 567);   print(car2.getProp())
car1.setProp(678, 'プリウス'); print(car1.getProp())
car1.setProp('プリウス', 678); print(car1.getProp())
