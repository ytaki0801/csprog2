class Car:
  def __init__(self, *props):
    if props:
      self.setProp(*props)
    else:
      self.setProp('', 0)
  def getProp(self):
    return self.__name + str(self.__num).zfill(4)
  def setProp(self, *props):
    name, num = props
    if isinstance(name, str):
      self.__name = name
    else:
      print('名前が文字列ではありません')
    if isinstance(num, int) and num < 10000 and num >= 0:
      self.__num = num
    else:
      print('ナンバーの値が不正です')

car1 = Car(); print(car1.getProp())
car2 = Car('カローラ', 567);   print(car2.getProp())
car1.setProp(678, 'プリウス'); print(car1.getProp())
car1.setProp('プリウス', 678); print(car1.getProp())
